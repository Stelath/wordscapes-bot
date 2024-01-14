import os
import string
from PIL import Image

import torch
import torch.nn.functional as F
from torch.utils.data import Dataset, DataLoader, Subset, random_split
from torchvision import transforms

class LettersDataset(Dataset):
    def __init__(self, dataset: str):
        self.dataset = dataset
        self.files = []
        for dirpath, dirnames, filenames in os.walk(dataset):
            for filename in sorted(filenames):
                self.files.append(os.path.join(dirpath, filename))

        self.transform = transforms.Compose([
            transforms.Resize((64, 64), antialias=True),
            transforms.ToTensor(),
        ])

    def __len__(self):
        return len(self.files)

    def __getitem__(self, idx):
        img_path = self.files[idx]
        img = Image.open(img_path).convert('L')
        img = self.transform(img)
        
        label = os.path.dirname(img_path).split('/')[-1]
        label = string.ascii_uppercase.index(label)
        label = F.one_hot(torch.tensor(label), num_classes=26)
        
        item = {
            'img': img,
            'target': label,
        }
        
        return item
