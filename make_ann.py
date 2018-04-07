ann_path = '/home/Public/quenotg/GINF53C4/PROJET/train/ann/'
concepts = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']
train_file_path = 'train/sortie_train.txt'

for concept in concepts:
	ann_file_path = ann_path+concept+'.ann'
	with open(ann_file_path, "r") as ann_file, open(train_file_path, "r") as train_file, open('train/color/color_'+concept+'.svm', "w") as res_file:
		for line_ann, line_train in zip(ann_file, train_file):
			stripped_line = line_ann[12:].strip()
			if int(stripped_line) != 0:
				res_file.write(stripped_line + line_train[1:])

