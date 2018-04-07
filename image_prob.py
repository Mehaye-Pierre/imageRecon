import os
import sys
import operator

concepts = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
dict = {}
sorted_x = []


os.system("./read_image "+sys.argv[1]+" > ./val/tmp.svm")
for concept in concepts:
    os.system("./libsvm-3.22/svm-predict -b 1 ./val/tmp.svm ./train/model/color_"+concept+".model"+" ./out/color_"+concept+".out")
for concept in concepts:
    with open("out/color_"+concept+".out", "r") as out_file :
        out_file.readline()
        line = out_file.readline()
        percent = float(line.split(' ')[1])
        dict[concept] = percent
        sorted_x = sorted(dict.items(), key=operator.itemgetter(1))
for i in range (1,6):
	print("Rang "+str(i) +": "+str(sorted_x[-i]))
