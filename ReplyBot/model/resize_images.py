import PIL
from PIL import Image
import os

rootin = './bigtidepod/'
rootout = './tidepod/'


for f in os.listdir(rootin):
    fulldir = rootin + f

    img = Image.open(fulldir)
    
    shortsize = min(img.size)
    factor = int(shortsize/224) -1

    img = img.resize((img.size[0]//factor,img.size[1]//factor), PIL.Image.ANTIALIAS)
    img.save(rootout + f)
