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


from sklearn.impute import SimpleImputer

from sklearn.svm import LinearSVR
from sklearn.svm import SVR
from sklearn.svm import SVC
from sklearn.multioutput import MultiOutputRegressor
from sklearn.multioutput import MultiOutputClassifier


from sklearn.naive_bayes import BernoulliNB

def KNN2(sa,clusters,k):
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
	
	for j in distances[0:k]:
		#print(j[1])
		Lat += float(dataset[j[1]][0])
		Lon += float(dataset[j[1]][1])
		
	#print(building)
	#print(b.most_common(1))
	#return ((Lon/k),(Lat/k), int(dataset[distances[0][1]][2]), int(dataset[distances[0][1]][3]) )
	return ((Lon/k),(Lat/k))




print("*"*70)
print("-"*50)
print("\n")
print("Beginnning data parsing and manipulation")
print("\n")


 # min N P K

#MAN1 -101 7 4 14
samples = []
dataset = []
with open('../../datasets/man1/MAN1_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../datasets/man1/MAN1_trncrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		dataset.append(row[:2]) # samples RSSI
		

samples2 = []
dataset2 = []
with open('../../datasets/man1/MAN1_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../datasets/man1/MAN1_tstcrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		dataset2.append(row[:2]) # samples RSSI

timeCL=0
time1 = time.time()
clusters=SAS.cluster_int(7, 4, samples, -101, "Cluster" )
#clusters=SAS.cluster2(7, 0.6, samples, -101, "Cluster" )
timeCL += time.time() - time1



for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i][:4]]
	samples[i] = [float(j) for j in samples[i]]


true_x = [] # Lat
true_y = [] # Long


for i in range(0,len(samples2)):
	#print(dataset2[i])
	true_x.append(float(dataset2[i][1]))
	true_y.append(float(dataset2[i][0]))

	#break



print("-"*50)
print("\n")
print("Beginnning cluster identification and Position estimation")
print("\n")


SASpredict_x = [] # Lat
SASpredict_y = [] # Long
timeSAS = 0
timeCI=0


for i in samples2:
	#print("-"*23)
	clusters_merge=[]
	
	time1 = time.time()
	#samples_in_cluster=SAS.cluster_identification2(i,clusters,samples, 6)
	samples_in_cluster=SAS.cluster_identification(i,clusters, 7,-101)
	#samples_in_cluster=SAS.cluster_identification_repetition(i,clusters, 6,-100)
	timeCI += time.time() - time1





	time1 = time.time()
	result = KNN2(i, samples_in_cluster, 14)
	timeSAS += time.time() - time1

	#print("-"*23)

	SASpredict_x.append(result[0])

	SASpredict_y.append(result[1])








SASError=[]
FError=[]
Normal = []
SASsumError = 0

EuclideanDistanceSAS = []
for k in range(0,len(true_y)):
	bF = np.array((true_x[k], true_y[k])).astype(float)
	sas = False
	aSAS = np.array((SASpredict_x[k], SASpredict_y[k])).astype(float)
	EuclideanDistanceSAS.append(np.linalg.norm(aSAS -bF))

	

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