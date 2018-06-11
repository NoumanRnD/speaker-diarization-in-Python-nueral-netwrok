 

import Featurecontroller
import os
import inputReciverLoad
import Diarization
import sys 
import csv
from matplotlib import pyplot


def read_Features(file):     
    base_pre_data = inputReciverLoad.get_wave_file(file)
    preprocessed = Diarization.speaker(base_pre_data)
    return FeatureExtractor.extract_mfcc_60(preprocessed)


def write_features(text, features):    
    for window in features:
        for feature in window:
            sys.stdout.write(str(feature)+",")
        print text


def print_head():    
    for index in range(60):  
        print "@Property " + str(index) + " feild"
    print "@Property class {Kamuran,Firat,Marvin}"
    print ""
    print "@DATA"

 
def main():     
    write_features("HEADER", read_Features("test.wav"))
    print_head()

def compare_j48_subtree_raising():
    
    pyplot.ylabel('accuracy')
    pyplot.xlabel('confidence')
    with open("J48_comparison.tsv", "r") as o:
        reader = csv.reader(o, delimiter="\t")
        for row in reader:
            break # discard for line
        row_with, row_without = [], []
        for row in reader:
            row_with += [(row[0], row[3]) if row[1] == "Yes" else None]
            row_without += [(row[0], row[3]) if row[1] == "No" else None]
    pyplot.plot([t[0] for t in row_with if t], [t[1] for t in row_with if t], "g^", label="With subtree raising")
    pyplot.plot([t[0] for t in row_without if t], [t[1] for t in row_without if t], "r+", label="Without subtree raising")
    pyplot.grid(True)
    pyplot.legend()
    pyplot.show() 


def compare_confidence_without_subtree_raising():
    pyplot.ylabel('accuracy')
    pyplot.xlabel('confidence')
    with open("J48_comparison.tsv", "r") as o:
        reader = csv.reader(o, delimiter="\t")
        for row in reader:
            break # discard for line
        for row in reader:
            if row[1] == "No":
                pyplot.plot(row[0], row[3], "bs", label="With subtree raising")
    pyplot.grid(True)
    pyplot.show() 


def compare_one_rule():
    pyplot.ylabel('accuracy')
    pyplot.xlabel('bucket size')
    with open("OneRule.tsv", "r") as o:
        reader = csv.reader(o, delimiter="\t")
        for row in reader:
            break 
        for row in reader:
            print row[0], row[1]
            g = pyplot.plot(float(row[0]), float(row[1]), "bs")
    pyplot.grid(True)
    pyplot.show() 


def random_beam():
    pyplot.ylabel('accuracy')
    pyplot.xlabel('forest size')
    with open("RandomForest.tsv", "r") as o:
        reader = csv.reader(o, delimiter="\t")
        for row in reader:
            break # discard for line
        for row in reader:
            print row[0], row[1]
            g = pyplot.plot(float(row[0]), float(row[1]), "bs")
    pyplot.grid(True)
    pyplot.show() 


def compare_layers():
    pyplot.ylabel('accuracy')
    pyplot.xlabel('number of epoches')
    with open("SingleLayerMultiLayerPerceptron.tsv", "r") as o:
        reader = csv.reader(o, delimiter="\t")
        for row in reader:
            break # discard for line
        row_0_1, row_0_2, row_0_3 = [], [], []
        for row in reader:
            row_0_1 += [(row[1], row[2]) if row[0] == "0.1" else None]
            row_0_2 += [(row[1], row[2]) if row[0] == "0.2" else None]
            row_0_3 += [(row[1], row[2]) if row[0] == "0.3" else None]
    pyplot.plot([t[0] for t in row_0_1 if t], [t[1] for t in row_0_1 if t], "g^", label="learning rate = 0.1")
    pyplot.plot([t[0] for t in row_0_2 if t], [t[1] for t in row_0_2 if t], "bs", label="learning rate = 0.2")
    pyplot.plot([t[0] for t in row_0_3 if t], [t[1] for t in row_0_3 if t], "r+", label="learning rate = 0.3")
    pyplot.grid(True)
    pyplot.legend(loc=4)
    pyplot.show() 
      
      
def check_alpha():
    pyplot.ylabel('accuracy')
    pyplot.xlabel('number of epoches')
    with open("SingleLayerMultiLayerPerceptron.tsv", "r") as o:
        reader = csv.reader(o, delimiter="\t")
        for row in reader:
            break # discard for line
        for row in reader:
            if row[0] == "0.1":
                pyplot.plot(float(row[1]), float(row[2]), "bs")             
    pyplot.grid(True)
    pyplot.show() 
    
            
        
        
        
main()
compare_layers()
