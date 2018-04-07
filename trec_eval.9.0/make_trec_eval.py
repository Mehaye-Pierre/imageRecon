rel_path = '/home/Public/quenotg/GINF53C4/PROJET/val/rel/'
concepts = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

import os


os.system('rm ../top/all.top')
for concept in concepts:
    os.system('./trec_eval '+rel_path+concept+'.rel '+'../top/'+concept+'.top > ../map/'+concept+'.txt')
    os.system('cat ../top/'+concept+'.top >> ../top/all.top')
os.system('./trec_eval '+rel_path+'all.rel '+'../top/all.top > ../map/all.txt')
