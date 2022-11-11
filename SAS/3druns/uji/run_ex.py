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
	s = np.array(sa).astype(int)
	for i in range(0,len(clusters)):
		samp= np.array(samples[clusters[i]]).astype(int)
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
	building = []
	floor = []

	k = min(len(distances),k)
	for j in distances[0:k]:
		#print(j[1])
		Lat += float(dataset[j[1]][0])
		Lon += float(dataset[j[1]][1])
		building.append(int(dataset[j[1]][3]))
		floor.append(int(dataset[j[1]][2]))
		#sp.append([j[1]])
	#SS.append(sp)
	b = Counter(building)
	f = Counter(floor)
	#print(building)
	#print(b.most_common(1))
	#return ((Lon/k),(Lat/k), int(dataset[distances[0][1]][2]), int(dataset[distances[0][1]][3]) )
	return ((Lon/k),(Lat/k), f.most_common(1)[0][0], b.most_common(1)[0][0])


print("*"*70)
print("-"*50)
print("\n")
print("Beginnning data parsing and manipulation")
print("\n")


 # min N P K
#UJI -105 2 0 7

samples = []
dataset = []
with open('../../datasets3d/trainingData3d.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row[:400]) # samples RSSI
		dataset.append(row[-4:])

	

#remove the labels row
samples.pop(0)
dataset.pop(0)
for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i][:4]]
	samples[i] = [int(j) for j in samples[i]]
timeCL=0
time1 = time.time()
clusters=SAS.cluster_int(5, 1, samples, -105, "Cluster" )
#clusters=SAS.cluster_recalculate_cluster_representatives(2, 0, samples, -105, "Cluster" )
#clusters=SAS.cluster2(2, 0.1, samples, -105, "Cluster" )

timeCL += time.time() - time1
#UJI

samples2 = []
dataset2 = []
#validationData_no_unDetected_no_bellow_treshold
#bad_samples
with open('../../datasets3d/validationData3d.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row[:400]) # samples RSSI
		dataset2.append(row[-4:])



samples2.pop(0)

dataset2.pop(0)















#clusters =SAS.remove_geomtricDistant_samples(dataset, clusters)


#exit()

#UJI

true_x = [] # Lat
true_y = [] # Long
true_f = [] # Floor
true_b = [] # Building


for i in range(0,len(samples2)):

	true_x.append(float(dataset2[i][1]))
	true_y.append(float(dataset2[i][0]))
	true_f.append(float(dataset2[i][2])) # 2UJI 4 sah1
	true_b.append(float(dataset2[i][3])) 
	#break




#UJI

SASpredict_x = [] # Lat
SASpredict_y = [] # Long
SASpredict_f = [] # Floor
SASpredict_b = [] # Building
timeSAS = 0
timeCI = 0

lc =[]
for i in samples2:
	#print("-"*23)
	clusters_merge=[]
	
	time1 = time.time()
	#samples_in_cluster=SAS.cluster_identification2(i,clusters,samples, 2)
	samples_in_cluster=SAS.cluster_identification(i,clusters, 5, -105)
	#samples_in_cluster=SAS.cluster_identification_repetition(i,clusters, 2, -105)
	timeCI += time.time() - time1

	lc.append(len(samples_in_cluster))



	time1 = time.time()
	result = KNN5(i, samples_in_cluster, 5)
	
	timeSAS += time.time() - time1

	#print("-"*23)

	SASpredict_x.append(result[0])

	SASpredict_y.append(result[1])


	SASpredict_f.append(float(result[2]))

	SASpredict_b.append(float(result[3]))
	#break






#print(sum(lc)/len(lc))
#EuclideanDistanceF = []
EuclideanDistanceSAS = []
#Fcomp = []
#SAScomp = []
for k in range(0,len(true_y)):
	bF = np.array((true_x[k], true_y[k], true_b[k], true_f[k])).astype(float)
	aSAS = np.array((SASpredict_x[k], SASpredict_y[k], SASpredict_b[k], SASpredict_f[k])).astype(float)


	
	EuclideanDistanceSAS.append(np.linalg.norm(aSAS -bF))

#print(SASpredict_x)
#print(true_x)
#print(SASpredict_y)
#print(true_y)
# Statistic values
print("SAS :")



print ("\t SAS Median: " + str(statistics.median(EuclideanDistanceSAS)) )

print ("\t SAS Average: " + str(sum(EuclideanDistanceSAS) / len(EuclideanDistanceSAS)) )


print("\t SAS Clustergin Time: " + str(timeCL))
print("\t SAS Cluster Identification Time: " + str(timeCI))
print("\t SAS KNN Time: " + str(timeSAS))
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

