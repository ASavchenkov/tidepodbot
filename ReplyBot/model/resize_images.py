import PIL
from PIL import Image
import os

rootin = './bigtidepod/'
rootout = './tidepod/'


for f in os.listdir(rootin):
    fulldir = rootin + f

    img = Image.open(fulldir)
    
    shortsize = min(img.size)
    factor = shortsize/260

    img = img.resize((int(img.size[0]//factor),int(img.size[1]//factor)), PIL.Image.ANTIALIAS)
    print(img.size)
    img.save(rootout + f)
