import torch
import torch.nn as nn
# import torch.nn.functional as F
from torch.autograd import Variable
from torchvision import models, transforms

import os
from PIL import Image

input_transform = transforms.Compose([
    transforms.Scale(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225]),
    ])

class Classifier:
    def __init__(self, param_path, try_gpu = True):
        self.model = models.resnet18()

        num_ftrs = self.model.fc.in_features
        self.model.fc = nn.Linear(num_ftrs, 2)
        self.model.load_state_dict(torch.load(param_path))
        self.model.train(False)
        
        self.use_gpu = try_gpu and torch.cuda.is_available()

        if self.use_gpu:
            self.model = self.model.cuda()

    #takes a PIL image, resizes to 256 by 256, and crops to 224, 244 
    #returns 0 if not tidepod, 1 if tidepod
    def classify_image(self, img):
        inTensor=  input_transform(img)
        inTensor = inTensor.unsqueeze(0)
        inTensor = inTensor.expand([-1,3,-1,-1])

        if self.use_gpu:
            inVar = Variable(inTensor.cuda())
        else:
            inVar = Variable(inTensor)
        
        output = self.model(inVar)
        print(output)
        _, pred = torch.max(output.data, 1)

        return pred.cpu().numpy()[0]



if __name__ == '__main__':
    rootdir = './data/val/tidepod/'

    classifier = Classifier('/.best_model')

    for f in os.listdir(rootdir):
        p = rootdir + f
        img = Image.open(p) 
        
        
        result = classifier.classify_image(img)
        if result==0:
            print(p)
