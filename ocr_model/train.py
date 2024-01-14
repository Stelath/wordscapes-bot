import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader, random_split

import lightning as L
from lightning.pytorch.callbacks import ModelCheckpoint

from dataset import LettersDataset
from model import WordscapesOCRModel

def main():
    dataset = LettersDataset('data/')
    train_dataset, val_dataset = random_split(dataset, [int(len(dataset) * 0.8), len(dataset) - int(len(dataset) * 0.8)])
    train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True, num_workers=5, persistent_workers=True)
    val_loader = DataLoader(val_dataset, batch_size=64, shuffle=False, num_workers=5, persistent_workers=True)
    
    model = WordscapesOCRModel()
    
    checkpoint_callback = ModelCheckpoint(
        monitor='val/loss',
        filename='ocr_model-{epoch:02d}-{val/loss:.2f}',
        save_top_k=3,
        mode='min',
    )
    
    trainer = L.Trainer(accelerator='mps', strategy='auto', devices='auto', max_epochs=40, callbacks=[checkpoint_callback], log_every_n_steps=5, val_check_interval=0.5)
    trainer.fit(model, train_loader, val_loader)

if __name__ == '__main__':
    main()
