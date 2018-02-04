import os
from shutil import copyfile
from random import shuffle

dirs = ['data/train/tidepod/',
        'data/train/negative/',
        'data/val/tidepod/',
        'data/val/negative/']

for d in dirs:
    if not os.path.exists(d):
        os.makedirs(d)


negroot = 'negative/'
podroot = 'tidepod/'

negatives = os.listdir(negroot)
pods = os.listdir(podroot)
shuffle(negatives)
shuffle(pods)

negsplit = int(0.7 * len(negatives))
podsplit = int(0.7 * len(pods))

negatives_train, negatives_val = negatives[:negsplit], negatives[negsplit:]
pods_train, pods_val = pods[:podsplit], pods[podsplit:]


for i,neg in enumerate(negatives_train):
    negpath = negroot + neg
    podpath = podroot + pods_train[i%len(pods_train)]
    print(negpath, podpath)
    copyfile(negpath, 'data/train/negative/negative' + str(i) + '.jpg')    
    copyfile(podpath, 'data/train/tidepod/tidepod' + str(i) + '.jpg')    

for i, neg in enumerate(negatives_val):
    negpath = negroot + neg
    podpath = podroot + pods_val[i%len(pods_val)]
    print(negpath, podpath)

    copyfile(negpath, 'data/val/negative/negative' + str(i) + '.jpg')    
    copyfile(podpath, 'data/val/tidepod/tidepod' + str(i) + '.jpg')    
