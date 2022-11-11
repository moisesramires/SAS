import time

import statistics
import matplotlib.pyplot as plt
import csv
import sys
import numpy as np
import plotly.graph_objects as go
import statistics
from collections import Counter
import json
import sys

def KNN5(sa,clusters,k):
	distances=[]
	samp=[]
	s = np.array(sa).astype(float)
	for i in range(0,len(clusters)):
		samp= np.array(samples[clusters[i]]).astype(float)
		dist = np.linalg.norm(s-samp)
		#dist = advanced_Euc(s,samp)
		distances.append((dist,clusters[i]))
	#print(distances[0])
	distances.sort(key=lambda x: x[0])
	#print("""""""""""")
	#print(cl)
	Lon = 0
	Lat = 0
	#sp = []
	floor = []
	for j in distances[0:k]:
		#print(j[1])
		Lat += float(dataset[j[1]][0])
		Lon += float(dataset[j[1]][1])
		floor.append(float(dataset[j[1]][2]))
		#sp.append([j[1]])
	#SS.append(sp)
	f = Counter(floor)
	#print(building)
	#print(b.most_common(1))
	#return ((Lon/k),(Lat/k), int(dataset[distances[0][1]][2]), int(dataset[distances[0][1]][3]) )
	return ((Lon/k),(Lat/k), f.most_common(1)[0][0])



#TUT5  -94 4
#_no_bellow_treshold
samples = []
dataset = []
with open('../../datasets/tut5/TUT5_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../datasets/tut5/TUT5_trncrd_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset.append(row) # samples RSSI
		
#print(dataset[53])
samples2 = []
dataset2 = []
with open('../../datasets/tut5/TUT5_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../datasets/tut5/TUT5_tstcrd_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset2.append(row) # samples RSS






















for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i]]
	samples[i] = [float(j) for j in samples[i]]
#writer = csv.writer(open('idealFULLK.csv', 'a', newline=''), delimiter = ";")




#len(dataset)
#12
#print(dataset[0])
writer = csv.writer(open('CDF_Plain.csv', 'w', newline=''), delimiter = ";")
for knm in [4]:
	timeF = 0
	time1 = 0

	true_x = [] # Lat
	true_y = [] # Long
	true_f = [] # Floor
	Fpredict_x = [] # Lat
	Fpredict_y = [] # Long
	Fpredict_f = [] # Floor
	clF = range(0,len(samples))
	for m in range(0,len(samples2)):
		true_x.append(float(dataset2[m][1]))
		true_y.append(float(dataset2[m][0]))
		true_f.append(float(dataset2[m][2])) # 2 UJI, 4 SAH1
		#print(true_x)
		#print(true_y)
	for m in range(0,len(samples2)):
		time1 = time.time()
		result = KNN5(samples2[m], clF, knm)
		timeF += time.time() - time1
		Fpredict_x.append(result[0])

		Fpredict_y.append(result[1])

		Fpredict_f.append(float(result[2]))

	
	FError=[]
	Normal = []
	FsumError = 0
	EuclideanDistanceF = []
	alld=[]
	#print(true_b[-10])
	#print(Fpredict_b[-10])
	for k in range(0,len(true_y)):
		bF = np.array((true_x[k], true_y[k], true_f[k])).astype(float)
		aF = np.array((Fpredict_x[k], Fpredict_y[k], Fpredict_f[k])).astype(float)


		
		EuclideanDistanceF.append(np.linalg.norm(aF -bF))

	print("F :")
	print(knm)

	print ("\t F Median: " + str(statistics.median(EuclideanDistanceF)) )

	print ("\t F Average: " + str(sum(EuclideanDistanceF) / len(EuclideanDistanceF)) )


	minimumF=np.amin(EuclideanDistanceF)
	print("\t F Minimum value: " + str(minimumF) )
	print("\t F Maximum value: " + str(np.amax(EuclideanDistanceF) ) )

	print("\t F Standard Deviation: " + str(np.std(EuclideanDistanceF)))

	print("\t F 25th percentile: ",
	       np.percentile(EuclideanDistanceF, 25))
	print("\t F 50th percentile: ",
	       np.percentile(EuclideanDistanceF, 50))
	print("\t F 75th percentile: ",
	       np.percentile(EuclideanDistanceF, 75))

	print("\t F Time: " + str(timeF))


	print("\n")
	print("*"*70)
	print("-"*50)
	print("\n")

	row=[str(knm),  str(sum(EuclideanDistanceF) / len(EuclideanDistanceF))]

	writer.writerow(row)

	for e in range(0,len(EuclideanDistanceF)):
		row=[str(EuclideanDistanceF[e])]
		writer.writerow(row)

