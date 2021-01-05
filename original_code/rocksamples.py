import math
from math import *

# read sample files

def load_data(data_input1, data_input2, weight):  
    with open(data_input1) as file1:
        lines1 = file1.readlines()
        data1 = []
        for line in lines1:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
            data1.append(row)
            
    with open(data_input2) as file2:
        lines2 = file2.readlines()
        data2 = []
        for line in lines2:
            row = []
            for n in line.split(','):
                row.append(float(n.strip()))
            data2.append(row)

    with open(weight) as filew:
        linew = filew.read()
        w = []
        for n in linew.split(','):
            w.append(float(n.strip()))
    
    return data1, data2, w

def results_X(data1, data2, w):
    results = []
    for i in range(len(data1)):
        s = 0
        for j in range(len(w)):
            if math.isnan(data1[i][j]) == False and math.isnan(data2[i][j]) == False:
                d = data1[i][j] - data2[i][j]
                s += w[j] * abs(d)
        results.append(s)
    return results
    
def results_Y(data1, data2, w):
    results = []
    for i in range(len(data1)):
        s = 0
        for j in range(len(w)):
            if math.isnan(data1[i][j]) == False and math.isnan(data2[i][j]) == False:
                d = (data1[i][j] - data2[i][j])**2
                s += w[j] * abs(d)
        results.append(s)    

def Algorithm_X(results):
    
    if analysis == 'd-index':
        dsum =  0
        for i in range(len(results)):
            dsum = dsum + (results[i])
        print("d-index:", dsum/len(results)) 

    if analysis == 'critical':
            critical = 0
            for i in range(len(results)):
                if results[i] > 5:
                    critical = critical + 1
            if critical == 1:
                print("criticality: 1 result above 5")
            else:
                print("criticality:", critical, "results above 5")

def Algorithm_Y(results):
    
    if analysis == 'd-index':
        dsum =  0
        for i in range(len(results)):
            dsum = dsum + sqrt(results[i])
        print("d-index:", dsum/len(results)) 
    
    if analysis == 'critical':
            critical = 0
            for i in range(len(results)):
                if results[i] > 5:
                    critical = critical + 1
            if critical == 1:
                print("criticality: 1 result above 5")
            else:
                print("criticality:", critical, "results above 5")


data_input1 = 'Coursework3\original_code\data1.csv'
data_input2 = 'Coursework3\original_code\data2.csv'
weight = 'Coursework3\original_code\weights.csv'
analysis = 'd-index'
algorithm ='y'
data1, data2, w = load_data(data_input1, data_input2, weight)

if algorithm == 'x':
    results = results_X(data1, data2, w)
    Algorithm_X(results)

if algorithm == 'y':
    results = results_Y(data1, data2, w)
    Algorithm_Y(results)
