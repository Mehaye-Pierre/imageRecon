import os

concepts = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']

for concept in concepts:
    os.system("./svm-train -w+1 19 -g 1.0 -b 1 ../train/color/color_"+concept+".svm ../train/model/color_"+concept+".model")

