concepts = ['aeroplane', 'bicycle', 'bird', 'boat', 'bottle', 'bus', 'car', 'cat', 'chair', 'cow', 'diningtable', 'dog', 'horse', 'motorbike', 'person', 'pottedplant', 'sheep', 'sofa', 'train', 'tvmonitor']



for concept in concepts :
    with open("out/color_"+concept+".out", "r") as out_file, open("list.txt", "r") as list_file, open('top/'+concept+'.top', "w") as top_file:
        out_file.readline();
        for line_out, line_list in zip(out_file, list_file):
            score = line_out.split(' ')[1]
            image = line_list[:-5]
            top_file.write(concept+" Q0 "+image+ " 0 "+score+" R"+'\n')