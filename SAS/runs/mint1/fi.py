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


def KNN3(sa,clusters,k):
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
	Lon = []
	Lat = []

	#sp = []
	#building = []
	#floor = []
	k = min(len(distances),k)
	for j in distances[0:k]:
		#print(j[1])
		#print(j[1])
		Lat.append(float(dataset[j[1]][0]))
		Lon.append(float(dataset[j[1]][1]))
		#building.append(int(dataset[j[1]][3]))
		#floor.append(int(dataset[j[1]][2]))
		#sp.append([j[1]])
	#SS.append(sp)
	la = Counter(Lat)
	lo = Counter(Lon)
	#print(building)
	#print((Lon/k))
	#print((Lat/k))
	#print(b.most_common(1))
	#return ((Lon/k),(Lat/k), int(dataset[distances[0][1]][2]), int(dataset[distances[0][1]][3]) )
	return (lo.most_common(1)[0][0],la.most_common(1)[0][0])






print("*"*70)
print("-"*50)
print("\n")
print("Beginnning data parsing and manipulation")
print("\n")


 # min N P K















print("-"*50)
print("\n")
print("Beginnning cluster identification and Position estimation")
print("\n")

writer = csv.writer(open('mint1.csv', 'a', newline=''), delimiter = ";")
writer.writerow(["N", "P",  "Median", "Average", "Minimum", "Maximum","Standard Deviation", "KNN Time", "CI TIme", "N#CL", "Clustering Time"])



#MINT1  -73 7 5 12
samples = []
dataset = []
with open('../../datasets/mint1/MINT1_trnrss.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../datasets/mint1/MINT1_trncrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		dataset.append(row[:2]) # samples RSSI
		
#print(dataset[53])
samples2 = []
dataset2 = []
with open('../../datasets/mint1/MINT1_tstrss.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../datasets/mint1/MINT1_tstcrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		dataset2.append(row[:2]) # samples RSS
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

for N in range(1,10):
	for P in range(0,N):
		SASpredict_x = [] # Lat
		SASpredict_y = [] # Long
		timeSAS = 0
		timeCI=0
		time1 = time.time()

		clusters=SAS.cluster_int(N, P, samples, -73, "Cluster" )
		timeCL = time.time() - time1

		for i in samples2:
			#print("-"*23)
			clusters_merge=[]
			
			time1 = time.time()
			#samples_in_cluster=SAS.cluster_identification2(i,clusters,samples, 7)
			samples_in_cluster=SAS.cluster_identification(i,clusters, N,-73)
			#samples_in_cluster=SAS.cluster_identification_repetition(i,clusters, 7,-73)
			timeCI += time.time() - time1





			time1 = time.time()
			result = KNN3(i, samples_in_cluster, 12)
			#result = SAS_SVM(i,samples_in_cluster)
			#result = SAS_BNB(i,samples_in_cluster)
			#print(result)
			timeSAS += time.time() - time1

			#print("-"*23)

			SASpredict_x.append(result[0])

			SASpredict_y.append(result[1])








		SASError=[]
		FError=[]
		Normal = []
		SASsumError = 0

		#EuclideanDistanceF = []
		EuclideanDistanceSAS = []
		#alld=[]
		#Fcomp = []
		#SAScomp = []
		for k in range(0,len(true_y)):
			bF = np.array((true_x[k], true_y[k])).astype(float)
			sas = False
			aSAS = np.array((SASpredict_x[k], SASpredict_y[k])).astype(float)
			EuclideanDistanceSAS.append(np.linalg.norm(aSAS -bF))

			

		#print(SASpredict_x)
		#print(true_x)
		#print(SASpredict_y)
		#print(true_y)
		# Statistic values
		print("SAS :")


		print ("\t SAS Median: " + str(statistics.median(EuclideanDistanceSAS)) )

		print ("\t SAS Average: " + str(sum(EuclideanDistanceSAS) / len(EuclideanDistanceSAS)) )


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
		row=[str(N*-1),str(P), str(statistics.median(EuclideanDistanceSAS)), str(sum(EuclideanDistanceSAS) / len(EuclideanDistanceSAS)), str(minimum),  str(np.amax(EuclideanDistanceSAS) ),  str(np.std(EuclideanDistanceSAS)), str(timeSAS),str(timeCI), str(len(clusters)),str(timeCL)  ] 
		writer.writerow(row)
