import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision
from torchvision import models, transoforms

input_transform = transforms.Compose([
    transoforms.Scale(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])


for file i
