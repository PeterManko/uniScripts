#!/usr/bin/env python3

from inspect import getfile
import re
import csv
from os.path import exists


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

def compute(rows):
    # perform calculations
    for row in rows:
        for i in range(len(row)):
            for j in reversed(range(len(row[i]))):
                if j != 0:
                    row[i][j-1] += row[i][j]/60
                    row[i].pop()

    return rows

def formatData(rows):

    # format vals for output
    for row in rows:
        for i in range(len(row)):
            row[i] = round(row[i][0], 9)
            row[i] = str(row[i])
            row[i]+= (9-len((row[i].split('.'))[1])) * '0'

    return rows

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
file = getFile()

rows, header = getData(file)

rows = compute(rows)

rows = formatData(rows)

outputFile(header, rows)