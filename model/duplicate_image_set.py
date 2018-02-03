from shutil import copyfile
import os


rootin = './smallTidepods/val/'
rootout='./images/val/tidepod/'


og_files = os.listdir(rootin)

for i in range(100):
    ogpath = rootin + og_files[i%len(og_files)]
    newpath= rootout + 'tidepod' + str(i) + '.jpg'
    print(ogpath, newpath)
    copyfile(ogpath, newpath)
