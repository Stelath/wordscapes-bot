import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import mobilenet_v3_small, mobilenet_v2

import lightning as L
import torchmetrics

class WordscapesOCRModel(L.LightningModule):
    def __init__(self):
        super().__init__()
        
        # self.model = mobilenet_v2()
        # self.model._modules["features"][0][0] = nn.Conv2d(1, 32, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        # self.model._modules["classifier"][1] = nn.Linear(in_features=1280, out_features=26, bias=True)
        
        # self.model = mobilenet_v3_small()
        # self.model._modules["features"][0][0] = nn.Conv2d(1, 16, kernel_size=(3, 3), stride=(2, 2), padding=(1, 1), bias=False)
        # self.model._modules["classifier"][3] = nn.Linear(in_features=1024, out_features=26, bias=True)
        
        self.model = nn.Sequential(
            nn.Conv2d(1, 16, 3),
            nn.Conv2d(16, 32, 3),
            nn.Conv2d(32, 16, 3),
            nn.Conv2d(16, 8, 3),
            nn.AvgPool2d(3),
            nn.Conv2d(8, 1, 3),
            nn.Flatten(),
            nn.Linear(256, 128),
            nn.Sigmoid(),
            nn.Linear(128, 64),
            nn.Sigmoid(),
            nn.Linear(64, 26)
        )
        
        self.loss_func = nn.CrossEntropyLoss()
    
    def forward(self, inp):
        return self.model(inp)
    
    def training_step(self, batch, batch_idx):
        inp, target = batch['img'], batch['target'].to(torch.float32)
        
        out = self(inp)
        
        loss = self.loss_func(out, target)
        
        self.log('train/loss', loss, on_step=True, on_epoch=True, prog_bar=True)
        self.log('train/acc', torch.mean((torch.argmax(out, dim=1) == torch.argmax(target, dim=1)).to(torch.float16)), on_step=True, on_epoch=True, prog_bar=True)
        
        return loss
    
    def validation_step(self, batch, batch_idx):
        inp, target = batch['img'], batch['target'].to(torch.float32)
        
        out = self(inp)
        
        loss = self.loss_func(out, target)
        
        self.log('val/loss', loss)
        self.log('val/acc', torch.mean((torch.argmax(out, dim=1) == torch.argmax(target, dim=1)).to(torch.float16)))
        
        return loss
    
    def configure_optimizers(self):
        return torch.optim.AdamW(self.parameters(), lr=1e-4)
    