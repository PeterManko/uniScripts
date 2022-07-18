#!/usr/bin/env python3

from inspect import getfile
import re
import csv
from os.path import exists

# preparing file to import from
def getFile():
    
    fileToProcess = input('Enter file location for processing: ')

    # check if file exists
    if not exists(fileToProcess):
        print("File does not exist! ")
        exit()


    # preapare file for reading
    fileToProcess = open(fileToProcess)
    fileToProcess = csv.reader(fileToProcess)

    return fileToProcess
# getting data out from file
def getData(fileToProcess):

    # read header and data
    header = next(fileToProcess)
    rows = []
    for row in fileToProcess:
        # format vals for calculations
        for i in range(len(row)):
        # check for reversed values
            if('E' in row[0]):
                row[0], row[1] = row[1], row[0]
            row[i] = re.sub("N|E", '', row[i])

            while row[i][-1] == '’' or row[i][-1] == "'":
                row[i] = row[i][:-1]
            row[i] = re.split("°|’|'", row[i])
            row[i] = [float(val) for val in row[i]]

        rows.append(row)
    return rows, header

# calculating all gps coordinates
def compute(rows):
    # perform calculations
    for row in rows:
        for i in range(len(row)):
            for j in reversed(range(len(row[i]))):
                if j != 0:
                    row[i][j-1] += row[i][j]/60
                    row[i].pop()

    return rows

# formatting data for output
def formatData(rows):

    # format vals for output
    for row in rows:
        for i in range(len(row)):
            row[i] = round(row[i][0], 9)
            row[i] = str(row[i])
            row[i]+= (9-len((row[i].split('.'))[1])) * '0'

    return rows
# writing data into file
def outputFile(header, rows):
    outputFile = input('Enter output file path: ')

    # prepare file for output
    with open(outputFile, 'w', encoding='UTF8', newline='') as f:
        writer = csv.writer(f)

        # write the header
        writer.writerow(header)

        # write multiple rows
        writer.writerows(rows)
    return True

# writing data into StdOut
def outputToStdOut(header, rows):
    for item in header:
        print(item, end=" ")

    for row in rows:
        for item in row:
            print(item, end=" ")


# methods used by main program

# full conversion into file
def covertToFile():

    file = getFile()

    rows, header = getData(file)

    rows = compute(rows)

    rows = formatData(rows)

    outputFile(header, rows)
# full conversion into StdOut
def convertToStdOut():
    file = getFile()

    rows, header = getData(file)

    rows = compute(rows)

    rows = formatData(rows)

    outputToStdOut(header, rows)
