import BSCv2

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
	k = min(len(distances),k)
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





samples = []
dataset = []
with open('../../../SAS_library/datasets/dsi/DSI1_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../../SAS_library/datasets/dsi/DSI1_trncrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset.append(row[:2]) # samples RSSI



samples2 = []
dataset2 = []
with open('../../../SAS_library/datasets/dsi/DSI1_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../../SAS_library/datasets/dsi/DSI1_tstcrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		dataset2.append(row[:2]) # samples RSSI


#UJI

true_x = [] # Lat
true_y = [] # Long

for i in range(0,len(samples2)):

	true_x.append(float(dataset2[i][1]))
	true_y.append(float(dataset2[i][0]))
	#break





for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i]]
	samples[i] = [float(j) for j in samples[i]]


writer = csv.writer(open('dsi.csv', 'a', newline=''), delimiter = ";")
#writer.writerow(["N", "Ts", "Median", "Average", "Minimum", "Maximum","Standard Deviation", "KNN Time", "CI Time","N#C", "CL Time"])
clF = range(0,len(samples))
#UJI
for Ts in [-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]:
	for N in range(5,8):
		BSCv2predict_x = [] # Lat
		BSCv2predict_y = [] # Long
		BSCv2predict_f = [] # Floor
		BSCv2predict_b = [] # Building
		timeBSCv2 = 0
		timeCI = 0

		timeCL=0
		time1 = time.time()
		clusters=BSCv2.cluster(1, Ts, samples, -100, -10 )
		#clusters=BSCv2.cluster_recalculate_cluster_representatives(2, 0, samples, -105, "Cluster" )
		#clusters=BSCv2.cluster2(2, 0.1, samples, -105, "Cluster" )

		timeCL += time.time() - time1


		lc =[]
		for i in samples2:
			#print("-"*23)
			clusters_merge=[]
			
			time1 = time.time()
			samples_in_cluster=BSCv2.cluster_identification_using_N_APS(i,clusters, N, -100)
			timeCI += time.time() - time1

			lc.append(len(samples_in_cluster))

			if (len(samples_in_cluster)>0):

				time1 = time.time()
				result = KNN2(i, samples_in_cluster, 30)
				
				timeBSCv2 += time.time() - time1

				#print("-"*23)

				BSCv2predict_x.append(result[0])

				BSCv2predict_y.append(result[1])
			else:
				time1 = time.time()
				result = KNN2(i, clF, 30)
				
				timeBSCv2 += time.time() - time1

				#print("-"*23)

				BSCv2predict_x.append(result[0])

				BSCv2predict_y.append(result[1])









		#print(sum(lc)/len(lc))
		#EuclideanDistanceF = []
		EuclideanDistanceBSCv2 = []
		#Fcomp = []
		#BSCv2comp = []
		for k in range(0,len(true_y)):
			bF = np.array((true_x[k], true_y[k])).astype(float)
			aBSCv2 = np.array((BSCv2predict_x[k], BSCv2predict_y[k])).astype(float)


			
			EuclideanDistanceBSCv2.append(np.linalg.norm(aBSCv2 -bF))

		#print(BSCv2predict_x)
		#print(true_x)
		#print(BSCv2predict_y)
		#print(true_y)
		# Statistic values
		print("BSCv2 :")

		print(Ts)

		print ("\t BSCv2 Median: " + str(statistics.median(EuclideanDistanceBSCv2)) )

		print ("\t BSCv2 Average: " + str(sum(EuclideanDistanceBSCv2) / len(EuclideanDistanceBSCv2)) )


		print("\t BSCv2 Clustergin Time: " + str(timeCL))
		print("\t BSCv2 Cluster Identification Time: " + str(timeCI))
		print("\t BSCv2 KNN Time: " + str(timeBSCv2))
		minimum=np.amin(EuclideanDistanceBSCv2)
		print("\t BSCv2 Minimum value: " + str(minimum) )
		print("\t BSCv2 Maximum value: " + str(np.amax(EuclideanDistanceBSCv2) ) )

		print("\t BSCv2 Standard Deviation: " + str(np.std(EuclideanDistanceBSCv2)))

		print("\t BSCv2 25th percentile: ",
		       np.percentile(EuclideanDistanceBSCv2, 25))
		print("\t BSCv2 50th percentile: ",
		       np.percentile(EuclideanDistanceBSCv2, 50))
		print("\t BSCv2 75th percentile: ",
		       np.percentile(EuclideanDistanceBSCv2, 75))



		print("\n")
		print("*"*70)
		print("-"*50)
		print("\n")


		row=[str(N),str(Ts), str(statistics.median(EuclideanDistanceBSCv2)), str(sum(EuclideanDistanceBSCv2) / len(EuclideanDistanceBSCv2)), str(minimum),  str(np.amax(EuclideanDistanceBSCv2) ),  str(np.std(EuclideanDistanceBSCv2)), str(timeBSCv2), str(timeCI),str(len(clusters)), str(timeCL)]
		writer.writerow(row)