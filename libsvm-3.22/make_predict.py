import os

concepts = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

for concept in concepts:
    os.system("./svm-predict -b 1 ../val/color.svm ../train/model/color_"+concept+".model"+" ../out/color_"+concept+".out")

