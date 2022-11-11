


import matplotlib.pyplot as plt
import csv

file = open("tut6_samples_used.csv")
csvreader = csv.reader(file, delimiter=";")
header = next(csvreader)
print(header)
rowsBSC = []
for row in csvreader:
    rowsBSC.append(row)
print(rowsBSC[0])
file.close()


BSC_Error= []

for i in rowsBSC:
	BSC_Error.append(float(i[3]))

file = open("SAS_tut6_used_samples.csv")
csvreader = csv.reader(file, delimiter=";")
header = next(csvreader)
print(header)
rowsSAS = []
for row in csvreader:
    rowsSAS.append(row)
print(rowsSAS[0])
file.close()

SAS_Error= []

for i in rowsSAS:
	SAS_Error.append(float(i[3]))


print(SAS_Error)
plt.plot(SAS_Error, BSC_Error, 'o', color='red');
plt.plot([0,90], [0,90], color='blue');
plt.xlabel("SAS_Error")
plt.ylabel("BSC_Error")
plt.legend()
plt.show()