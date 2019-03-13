#!/usr/bin/env python
import sys
import shutil
from progress_bar import progressBar

def format_filename(name, number):
    num_zeros = "0"*(4 - len(number))
    filepath = "lfw-deepfunneled/"+name+"/"+name+"_"+num_zeros+number+".jpg"
    return filepath
'''
def make_csv(old_filename,new_filename):
    with open (old_filename) as fin, open(new_filename,'w') as fout:
        for line in fin:
            fout.write(line.replace('\t',' , '))
'''
def split(people_file,trainSets,valSets,testSets):
    fileLength = sum(1 for line in open(people_file))
    count = 0
    currentSet = 0
    valIndex = trainSets
    testIndex = trainSets + valSets
    currentDir = 0 #0 = train , 1 = val, 2 = test
    dirs = ["lfw_training","lfw_validation","lfw_testing"]
    with open(people_file) as my_file:
        for line in my_file:
            if count == 0:
                count +=1
                continue
            if any(c.isalpha() for c in line):
                s = line.strip("\n").split('\t')
                filepath = format_filename(s[0],s[1])
                shutil.copy(filepath,dirs[currentDir])
            else:
                currentSet += 1
                if currentSet == valIndex:
                    currentDir = 1
                elif currentSet == testIndex:
                    currentDir = 2
            if count % 50 == 0:
                progressBar("Splitting",count,fileLength)
            count += 1
    sys.stdout.flush()
def main(argv):
    split(argv[0],int(argv[1]),int(argv[2]),int(argv[3]))

if __name__ == '__main__':
    if len(sys.argv) > 5:
        print("Usage: python split.py [people text file] [numTrainSets] [numValidationSets] [numTestSets]")
        #sys.exit(0)
    else:
        main(sys.argv[1:])
