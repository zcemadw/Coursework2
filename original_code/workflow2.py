from math import *
import math
# read sample files

Algorithm = 2

#with open('data1.csv') as file1:
with open('Coursework3\original_code\samples1.csv') as file1:
    lines1 = file1.readlines()
    data1 = []
    for line in lines1:
        row = []
        for n in line.split(','):
            row.append(float(n.strip()))
        data1.append(row)

#with open('data2.csv') as file1:
with open('Coursework3\original_code\samples2.csv') as file2:
    lines2 = file2.readlines()
    data2 = []
    for line in lines2:
        row = []
        for n in line.split(','):
            row.append(float(n.strip()))
        data2.append(row)

with open('Coursework3\original_code\weights.csv') as filew:
    linew = filew.read()
    w = []
    for n in linew.split(','):
        w.append(float(n.strip()))

results = []

if Algorithm == 1:
    for i in range(len(data1)):
        s = 0
        for j in range(len(w)):
            if math.isnan(data1[i][j]) == False and math.isnan(data2[i][j]) == False:
                d = data1[i][j] - data2[i][j]
                s += w[j] * abs(d)
        results.append(s)

if Algorithm == 2:

    for i in range(len(data1)):
        s = 0
        for j in range(len(w)):
            if math.isnan(data1[i][j]) == False and math.isnan(data2[i][j]) == False:
                d = (data1[i][j] - data2[i][j])**2
                s += w[j] * abs(d)
        results.append(s)
        
# critical = 0
# for i in range(len(results)):
#     if results[i] > 5:
#         critical = critical + 1
# if critical == 1:
#     print("criticality: 1 result over 5")
# else:
#     print("criticality:", critical, "results over 5")
dsum =  0
for i in range(len(results)):
    dsum = dsum + sqrt(results[i])
print("d-index:", dsum/len(results))
