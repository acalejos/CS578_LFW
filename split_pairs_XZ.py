#!/usr/bin/env python
import sys
import shutil
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

def format_filename(name, number):
    num_zeros = "0"*(4 - len(number))
    filepath = "../lfw-deepfunneled/"+name+"/"+name+"_"+num_zeros+number+".jpg"
    return filepath


def split(train_file, test_file, train_same, train_diff, vali_same, vali_diff, test_same, test_diff):
    file_handler = open(train_file, "r", encoding="utf-8");
    for row in file_handler:
        temp=row.replace("\n", "");
        string= temp.split("\t"); # split it by whitespace
        converted = [x for x in string]
        if len(converted) ==3:
            train_same.append(converted);
        if len(converted) ==4:
            train_diff.append(converted);
    file_handler.close()
    
        
    file_handler = open( test_file, "r", encoding="utf-8")
    # We must first put the data in a list	
    for row in file_handler:
        temp=row.replace("\n", "");
        string= temp.split("\t") # split it by whitespace
        converted = [x for x in string]
        if len(converted) ==3:
            test_same.append(converted);
        if len(converted) ==4:
            test_diff.append(converted);
    file_handler.close()
    
    for i in range(len(test_same)//2):
        vali_same.append( test_same.pop() );
    
    for i in range( len(test_diff)//2 ):
        vali_diff.append( test_diff.pop() );
    
    print(len(train_same), len(vali_same), len(test_same) );
	
def get_image_plot(train_same, vali_same, test_diff):
	plt.figure();
	plt.subplot(3, 2, 1)
	img=mpimg.imread(format_filename(train_same[0][0], train_same[0][1] )  )
	imgplot = plt.imshow(img)
	plt.title(train_same[0][0]);
	plt.xticks([])
	plt.yticks([])
	
	plt.subplot(3, 2, 2)
	img=mpimg.imread(format_filename(train_same[0][0], train_same[0][2] )  )
	imgplot = plt.imshow(img)
	plt.title(train_same[0][0]);
	plt.xticks([])
	plt.yticks([])
	
	plt.subplot(3, 2, 3)
	img=mpimg.imread(format_filename(vali_same[0][0], vali_same[0][1] )  )
	imgplot = plt.imshow(img)
	plt.title(vali_same[0][0]);
	plt.xticks([])
	plt.yticks([])
	
	plt.subplot(3, 2, 4)
	img=mpimg.imread(format_filename(vali_same[0][0], vali_same[0][2] )  )
	imgplot = plt.imshow(img)
	plt.title(vali_same[0][0]);
	plt.xticks([])
	plt.yticks([])
	
	plt.subplot(3, 2, 5)
	img=mpimg.imread(format_filename(test_diff[0][0], test_diff[0][1] )  )
	imgplot = plt.imshow(img)
	plt.title(test_diff[0][0]);
	plt.xticks([])
	plt.yticks([])
	
	plt.subplot(3, 2, 6)
	img=mpimg.imread(format_filename(test_diff[0][2], test_diff[0][3] )  )
	imgplot = plt.imshow(img)
	plt.title(test_diff[0][2]);
	plt.xticks([])
	plt.yticks([])
	
	plt.tight_layout()
	plt.show()
	
def main():
	train_file="../pairsDevTrain.txt";
	test_file= "../pairsDevTest.txt";
	train_same=[];
	train_diff=[];
	vali_same=[];
	vali_diff=[];
	test_same= [];
	test_diff= [];
	
	split(train_file, test_file, train_same, train_diff, vali_same, vali_diff, test_same, test_diff);
	get_image_plot(train_same, vali_same, test_diff);
	
if __name__ == '__main__':
	main();
	
	
	
