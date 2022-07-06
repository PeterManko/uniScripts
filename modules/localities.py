#!/usr/bin/env python3

import csv
import sys

# reading csv and setting output into file
def init():
    fileName = input("Enter file name to work on:")
    file = open(fileName)
    file_path = fileName + '_Compared' # adding _Comapred into filename of of file for unique name
    sys.stdout = open(file_path, "w") # setting stdout into file
    
    return file

# function for comparing 2 rows
def compareAB(paramA, paramB):
    # init of vars
    first = 0
    second = 0
    both = 0
    # going trough columns 1 by 1
    for id, a in enumerate(paramA):
            # if 1 in both
            if a + paramB[id] >1:
                both+=1
            # if 1 in a and 0  in b 
            elif a>paramB[id]:
                first+=1
            # if 0 in a and 1 in b
            elif a<paramB[id]:
                second+=1
    out = str(both) + ',' + str(second) + ',' + str(first)
    #returning as str
    return out

file = init()
# reading whole file
csvreader = csv.reader(file)
rows = list()
# going trought rows of file and adding them into rows
for row in csvreader:
    rows.append([int(i) for i in row[1:]])
#going trough rows and comparing them
for i, a in enumerate(rows[:-1]):
    for b in rows[i+1:]:
        print(compareAB(a,b))
# closing file
file.close()