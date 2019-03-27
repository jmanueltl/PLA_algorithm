import csv
import sys
import numpy as np
# coding=utf-8

def load_data(input_data):
    data = []
    f = open(input_data)
    csv_f = csv.reader(f)
    for row in csv_f:
        for i in range (0,3):
            row[i] = int(row[i])
        data.append(row)
    return data

def sign(row, weight):
    s = ((weight[0] * row[0]) + (weight[1] * row[1]) + weight[2])
    if s > 0:
        return 1
    else:
        return -1

#Algoritm
def perceptronAlgorithm(data):
    weight = [0 for i in range(len(data[0]))]
    output = []
    while True:
        end = True
        for i in range(0, len(data)):
            expected = data[i][2]
            predict = sign(data[i], weight)
            if expected * predict <= 0:
                end = False
                weight[0] = weight[0] + expected * data[i][0]
                weight[1] = weight[1] + expected * data[i][1]
                weight[2] = weight[2] + expected

        if end:
            output.append([weight[0], weight[1], weight[2]])
            break
        else:
            output.append([weight[0], weight[1], weight[2]])
            
    return output
    
def write_data(output_data,output):    
    with open(output_data, 'w') as outcsv:
        writer = csv.writer(outcsv, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        for item in output:
            writer.writerow([item[0], item[1], item[2]])  

if __name__ == "__main__":
    input_data = sys.argv[1]
    output_data = sys.argv[2]
    data = load_data(input_data)
    output = perceptronAlgorithm(data)
    write_data(output_data,output)