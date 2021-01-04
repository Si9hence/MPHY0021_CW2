from math import *

# read sample files

with open('data1.csv') as file1:
    lines1 = file1.readlines()
    data1 = []
    for line in lines1:
        row = []
        for n in line.split(','):
            row.append(float(n.strip()))
        data1.append(row)

with open('data2.csv') as file2:
    lines2 = file2.readlines()
    data2 = []
    for line in lines2:
        row = []
        for n in line.split(','):
            row.append(float(n.strip()))
        data2.append(row)

with open('weights.csv') as filew:
    linew = filew.read()
    w = []
    for n in linew.split(','):
        w.append(float(n.strip()))

results = []
for i in range(len(data1)):
    s = 0
    for j in range(len(w)):
        d = data1[i][j] - data2[i][j]
        s += w[j] * abs(d)
    results.append(s)

critical = 0
for i in range(len(results)):
    if results[i] > 5:
        critical = critical + 1
if critical == 1:
    print("criticality: 1 result above 5")
else:
    print("criticality:", critical, "results above 5")
