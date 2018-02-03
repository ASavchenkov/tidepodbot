import torch
import torch.nn as nn
from torch.autograd import Variable
import torchvision
from torchvision import models, transforms

import os
import PIL
from PIL import Image

input_transform = transforms.Compose([
    transforms.Scale(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])

rootdir = './images/val/tidepod/'

use_gpu = torch.cuda.is_available() and True

model_ft = models.resnet18()
num_ftrs = model_ft.fc.in_features
model_ft.fc = nn.Linear(num_ftrs, 2)
model_ft.load_state_dict(torch.load('./best_model'))
model_ft.train(False)

if use_gpu:
    model_ft = model_ft.cuda()

for f in os.listdir(rootdir):
    p = rootdir + f
    img = Image.open(p) 
    
    inTensor=  input_transform(img)
    inTensor = inTensor.unsqueeze(0)
    inTensor = inTensor.expand([-1,3,-1,-1])

    if use_gpu:
        inVar = Variable(inTensor.cuda())
    else:
        inVar = Variable(inTensor)
    
    output = model_ft(inVar)
    _, pred = torch.max(output.data, 1)
    print(pred)
    
