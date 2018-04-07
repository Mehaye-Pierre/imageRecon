import sys



def parseFile(color,train) :
    fp1 = open(color, 'r')
    fp2 = open(train, 'r')
    fp3 = open('parseResult.svm','w')
    line1 = fp1.readline()
    line2 = fp2.readline()
    while len(line1) > 2:
        a = line1[1:]
        b = line2.split(' ', 1)[1]
        if b != '0' :
            fp3.write(a.strip()+b)
        line1 = fp1.readline()
        line2 = fp2.readline()
    fp1.close()
    fp2.close()
    fp3.close()


parseFile(sys.argv[1],sys.argv[2])
