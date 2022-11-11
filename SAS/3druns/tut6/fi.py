import SAS

import time

import matplotlib.pyplot as plt
import csv
import sys
import numpy as np
import plotly.graph_objects as go
import statistics
from collections import Counter
import json
import sys

import json



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
	k = min(len(distances),k)
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





print("*"*70)
print("-"*50)
print("\n")
print("Beginnning data parsing and manipulation")
print("\n")

print("-"*50)
print("\n")
print("Beginnning clustering")
print("\n")

#TUT6  -95  7 0 1
#_no_bellow_treshold
samples = []
dataset = []
with open('../../datasets/tut6/TUT6_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../datasets/tut6/TUT6_trncrd_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset.append(row) # samples RSSI
		
#print(dataset[53])
samples2 = []
dataset2 = []
with open('../../datasets/tut6/TUT6_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../datasets/tut6/TUT6_tstcrd_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset2.append(row) # samples RSS


true_x = [] # Lat
true_y = [] # Long
true_f = [] # Long
true_b = [] # Long


for i in range(0,len(samples2)):
	#print(dataset2[i])
	true_x.append(float(dataset2[i][1]))
	true_y.append(float(dataset2[i][0]))
	true_f.append(float(dataset2[i][2])) # 2 UJI, 4 SAH1

	#break



for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i]]
	samples[i] = [float(j) for j in samples[i]]
#writer = csv.writer(open('idealFULLK.csv', 'a', newline=''), delimiter = ";")

print("-"*50)
print("\n")
print("Beginnning cluster identification and Position estimation")
print("\n")

writer = csv.writer(open('test_tut6.csv', 'a', newline=''), delimiter = ";")
writer.writerow(["N", "P", "Median", "Average", "Minimum", "Maximum","Standard Deviation", "KNN Time", "CI Time", "N#C", "Clustering Time"])

#UJI
for N in range(1,12):
	for P in range(0,N):
		SASpredict_x = [] # Lat
		SASpredict_y = [] # Long
		SASpredict_f = [] # Floor
		timeSAS = 0

		time1 = time.time()
		clusters=SAS.cluster_int(N, P, samples, -95, "Cluster" )
		timeCL = time.time() - time1
		SASpredict_x = [] # Lat
		SASpredict_y = [] # Long
		timeSAS = 0

		timeCI = 0
		for i in samples2:
			#print("-"*23)
			clusters_merge=[]
			time1 = time.time()

			samples_in_cluster=SAS.cluster_identification(i,clusters, N,-95)
			#print(len(samples_in_cluster))
			


			timeCI += time.time() - time1
			time1 = time.time()


			result = KNN5(i, samples_in_cluster, 1)
			#result = SAS_SVM(i,samples_in_cluster)
			#result = SAS_BNB(i,samples_in_cluster)
			#print(result)
			timeSAS += time.time() - time1

			#print("-"*23)

			SASpredict_x.append(result[0])

			SASpredict_y.append(result[1])

			SASpredict_f.append(float(result[2]))

			#break






		SASError=[]
		FError=[]
		Normal = []
		SASsumError = 0

		#EuclideanDistanceF = []
		EuclideanDistanceSAS = []
		alld=[]
		#Fcomp = []
		#SAScomp = []
		for k in range(0,len(true_y)):
			bF = np.array((true_x[k], true_y[k], true_f[k])).astype(float)
			aSAS = np.array((SASpredict_x[k], SASpredict_y[k], SASpredict_f[k])).astype(float)


			
			EuclideanDistanceSAS.append(np.linalg.norm(aSAS -bF))
			

	
		print("SAS :")
		print(N)
		print(P)
		
		print ("\t SAS Median: " + str(statistics.median(EuclideanDistanceSAS)) )

		print ("\t SAS Average: " + str(sum(EuclideanDistanceSAS) / len(EuclideanDistanceSAS)) )


		print("\t Time: " + str(timeSAS))
		minimum=np.amin(EuclideanDistanceSAS)
		print("\t SAS Minimum value: " + str(minimum) )
		print("\t SAS Maximum value: " + str(np.amax(EuclideanDistanceSAS) ) )

		print("\t SAS Standard Deviation: " + str(np.std(EuclideanDistanceSAS)))

		print("\t SAS 25th percentile: ",
		       np.percentile(EuclideanDistanceSAS, 25))
		print("\t SAS 50th percentile: ",
		       np.percentile(EuclideanDistanceSAS, 50))
		print("\t SAS 75th percentile: ",
		       np.percentile(EuclideanDistanceSAS, 75))


		

		print("\n")
		print("*"*70)
		print("-"*50)
		print("\n")



		row=[str(N*-1),str(P), str(statistics.median(EuclideanDistanceSAS)), str(sum(EuclideanDistanceSAS) / len(EuclideanDistanceSAS)), str(minimum),  str(np.amax(EuclideanDistanceSAS) ),  str(np.std(EuclideanDistanceSAS)), str(timeSAS), str(timeCI),str(len(clusters)),str(timeCL)]
		writer.writerow(row)

