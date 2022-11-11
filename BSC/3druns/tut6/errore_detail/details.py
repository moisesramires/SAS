


import matplotlib.pyplot as plt
import csv



t=-10



file = open("tut6_samples_used.csv")
csvreader = csv.reader(file, delimiter=";")
header = next(csvreader)
print(header)
rowsBSC = []
for row in csvreader:
    rowsBSC.append(row)
file.close()


BSC_Error= []
order_rowsBSC = rowsBSC.copy()
order_rowsBSC.sort(key=lambda x: float(x[4]))

BSC_Error = order_rowsBSC[t:]





file = open("SAS_tut6_used_samples.csv")
csvreader = csv.reader(file, delimiter=";")
header = next(csvreader)
print(header)
rowsSAS = []
for row in csvreader:
    rowsSAS.append(row)
file.close()

SAS_Error= []
order_rowsSAS= rowsSAS.copy()
order_rowsSAS.sort(key=lambda x: float(x[4]))

SAS_Error = order_rowsSAS[t:]




file = open("Plain_tut6_used_samples.csv")
csvreader = csv.reader(file, delimiter=";")
header = next(csvreader)
print(header)
rowsPlain = []
for row in csvreader:
    rowsPlain.append(row)
file.close()

Plain_Error= []
order_rowsPlain =  rowsPlain.copy()
order_rowsPlain.sort(key=lambda x: float(x[4]))

Plain_Error = order_rowsPlain[t:]



samples_used = []
plain = []
sas = []
bsc = []

print("-"*50)

print(len(Plain_Error))
print(len(SAS_Error))
print(len(BSC_Error))
print("-"*50)


for i in range(0,t*-1):
	if Plain_Error[i][0] not in samples_used:
		samples_used.append(Plain_Error[i][0] )
	plain.append(Plain_Error[i][0] )

	if SAS_Error[i][0] not in samples_used:
		samples_used.append(SAS_Error[i][0] )
	sas.append(SAS_Error[i][0] )

	if BSC_Error[i][0] not in samples_used:
		samples_used.append(BSC_Error[i][0] )
	bsc.append(BSC_Error[i][0] )


for i in range(0,len(samples_used)):
	if samples_used[i] not in plain:
		Plain_Error.append(rowsPlain[int(samples_used[i])])

	if samples_used[i] not in sas:
		SAS_Error.append(rowsSAS[int(samples_used[i])])

	if samples_used[i] not in bsc:
		BSC_Error.append(rowsBSC[int(samples_used[i])])




print(samples_used)
print(len(samples_used))
print(len(Plain_Error))
print(len(SAS_Error))
print(len(BSC_Error))
print("-"*50)
Plain_Error.sort(key=lambda x: float(x[0]))
SAS_Error.sort(key=lambda x: float(x[0]))
BSC_Error.sort(key=lambda x: float(x[0]))

p=0
s=0
b=0
Ap=[float(a_tuple[4]) for a_tuple in Plain_Error]
As=[float(a_tuple[4]) for a_tuple in SAS_Error]
Ab=[float(a_tuple[4]) for a_tuple in BSC_Error]
for i in range(0,len(Plain_Error)):
	m = min ( float(Plain_Error[i][4]), float(SAS_Error[i][4]), float(BSC_Error[i][4]) )
	if (float(Plain_Error[i][4])==m):
		p+=1
	if (float(SAS_Error[i][4])==m):
		s+=1
	if (float(BSC_Error[i][4])==m):
		b+=1
print(Ap)

ap=(sum(Ap)/len(Ap))
ass=(sum(As)/len(As))
ab=(sum(Ab)/len(Ab))

print("*"*15)
print("Plain")
print("Wins/Ties: " + str(p))
print("Averages: " + str(ap))

print("*"*15)
print("SAS")
print("Wins/Ties: " + str(s))
print("Averages: " + str(ass))

print("*"*15)
print("BSC")
print("Wins/Ties: " + str(b))
print("Averages: " + str(ab))


writer = csv.writer(open('10_Plain.csv', 'a', newline=''), delimiter = ";")
writer.writerow(["Testing","Testing RSSI" ,"Estimated", "True", "Error", "Training", "Training RSSI", "Feature distance", "cluster"])
for row in Plain_Error:
	writer.writerow(row)

writer = csv.writer(open('10_SAS.csv', 'a', newline=''), delimiter = ";")
writer.writerow(["Testing","Testing RSSI" ,"Estimated", "True", "Error", "Training", "Training RSSI", "Feature distance", "cluster"])
for row in SAS_Error:
	writer.writerow(row)

writer = csv.writer(open('10_BSC.csv', 'a', newline=''), delimiter = ";")
writer.writerow(["Testing","Testing RSSI" ,"Estimated", "True", "Error", "Training", "Training RSSI", "Feature distance", "cluster"])
for row in BSC_Error:
	writer.writerow(row)






fig, (ax1, ax2) = plt.subplots(1, 2)
fig.suptitle('Horizontally stacked subplots')


x = range(0,len(samples_used))
ax1.plot(x, [float(a_tuple[4]) for a_tuple in Plain_Error], 'o', color='red',label="Plain");

ax1.plot(x, [float(a_tuple[4]) for a_tuple in SAS_Error], 'o', color='green', label="SAS");

ax1.plot(x, [float(a_tuple[4]) for a_tuple in BSC_Error], 'o', color='blue', label="BSC");
ax1.set_xlabel("sample")
ax1.set_ylabel("Error")

ax1.legend(prop={'size': 22})


ax2.plot(x, [float(a_tuple[7]) for a_tuple in Plain_Error], 'o', color='red',label="Plain");

ax2.plot(x, [float(a_tuple[7]) for a_tuple in SAS_Error], 'o', color='green', label="SAS");

ax2.plot(x, [float(a_tuple[7]) for a_tuple in BSC_Error], 'o', color='blue', label="BSC");
ax2.set_xlabel("sample")
ax2.set_ylabel("Feat. distance")

ax2.legend(prop={'size': 22})
plt.show()

