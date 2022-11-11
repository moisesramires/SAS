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


#LIB2 -100 6 2 24

samples = []
dataset = []

with open('../../datasets3d/lib2/LIB2_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		
with open('../../datasets3d/lib2/LIB2_tstcrd3d.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset.append(row[:3]) # samples RSSI
		
print("-"*50)
print("\n")
print("Beginnning clustering")
print("\n")



#LIB2 

samples2 = []
dataset2 = []
with open('../../datasets3d/lib2/LIB2_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI

with open('../../datasets3d/lib2/LIB2_trncrd3d.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset2.append(row[:3]) # samples RSSI




true_x = [] # Lat
true_y = [] # Long
true_f = [] # Long

for i in range(0,len(samples2)):

	true_x.append(float(dataset2[i][1]))
	true_y.append(float(dataset2[i][0]))
	#break
	true_f.append(float(dataset2[i][2]))

print("-"*50)
print("\n")
print("Beginnning cluster identification and Position estimation")
print("\n")

writer = csv.writer(open('CDF_SAS.csv', 'w', newline=''), delimiter = ";")


#3 0
#4 0
for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i][:4]]
	samples[i] = [int(j) for j in samples[i]]


# 6 0
# 10 0
for N in  range(6,7):
	for P in range(1,2):
	#for P in range(0,N):
		time1 = time.time()
		clusters=SAS.cluster_int(N, P, samples, -100, "Cluster" )
		timeCL = time.time() - time1
		SASpredict_x = [] # Lat
		SASpredict_y = [] # Long
		SASpredict_f = [] # Floor
		SASpredict_b = [] # Building
		timeSAS = 0
		timeCI = 0


		for i in samples2:
			#print("-"*23)
			clusters_merge=[]
			time1 = time.time()

			#samples_in_cluster=SAS.cluster_identification2(i,clusters,samples, 3)
			samples_in_cluster=SAS.cluster_identification(i,clusters, N, -100)
			#samples_in_cluster=SAS.cluster_identification_repetition(i,clusters, 3)
			
			timeCI += time.time() - time1




			
			time1 = time.time()
			result = KNN5(i, samples_in_cluster, 24)
			#result = SAS_SVM(i,samples_in_cluster)
			#result = SAS_BNB(i,samples_in_cluster)
			#print(result)
			timeSAS += time.time() - time1

			#print("-"*23)

			SASpredict_x.append(result[0])

			SASpredict_y.append(result[1])

			#break
			
			SASpredict_f.append(float(result[2]))

		row =[]




		SASError=[]
		FError=[]
		Normal = []
		SASsumError = 0

		#EuclideanDistanceF = []
		EuclideanDistanceSAS = []
		for k in range(0,len(true_y)):
			bF = np.array((true_x[k], true_y[k], true_f[k])).astype(float)
			aSAS = np.array((SASpredict_x[k], SASpredict_y[k], SASpredict_f[k])).astype(float)


			
			EuclideanDistanceSAS.append(np.linalg.norm(aSAS -bF))

			
			

		#print(SASpredict_x)
		#print(true_x)
		#print(SASpredict_y)
		#print(true_y)
		# Statistic values
		print("SAS :")

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
		row=[str(N), str(P),  str(sum(EuclideanDistanceSAS) / len(EuclideanDistanceSAS))]

		writer.writerow(row)

		for e in range(0,len(EuclideanDistanceSAS)):
			row=[str(EuclideanDistanceSAS[e])]
			writer.writerow(row)