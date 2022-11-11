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





#MINT1  -73 7 5 12
samples = []
dataset = []
with open('../../../SAS_library/datasets/mint1/MINT1_trnrss.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../../SAS_library/datasets/mint1/MINT1_trncrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		dataset.append(row[:2]) # samples RSSI
		
#print(dataset[53])
samples2 = []
dataset2 = []
with open('../../../SAS_library/datasets/mint1/MINT1_tstrss.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../../SAS_library/datasets/mint1/MINT1_tstcrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		dataset2.append(row[:2]) # samples RSS
for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i][:4]]
	samples[i] = [round(float(j)) for j in samples[i]]



for i in range(0,len(samples2)):
	samples2[i] = [round(float(j)) for j in samples2[i]]


#clusters =BSCv2.remove_geomtricDistant_samples(dataset, clusters)


#exit()


clF = range(0,len(samples))
true_x = [] # Lat
true_y = [] # Long
for i in range(0,len(samples2)):

	true_x.append(float(dataset2[i][1]))
	true_y.append(float(dataset2[i][0]))
	#break


writer = csv.writer(open('mint1.csv', 'a', newline=''), delimiter = ";")
writer.writerow(["N", "Ts", "Median", "Average", "Minimum", "Maximum","Standard Deviation", "KNN Time", "CI Time","N#C", "CL Time"])

#UJI
for Ts in [-1,-2,-3]:
	for N in range(1,2):
		BSCv2predict_x = [] # Lat
		BSCv2predict_y = [] # Long
		BSCv2predict_f = [] # Floor
		BSCv2predict_b = [] # Building
		timeBSCv2 = 0
		timeCI = 0

		timeCL=0
		time1 = time.time()
		clusters=BSCv2.cluster(1, Ts, samples, -73, -10 )
		#clusters=BSCv2.cluster_recalculate_cluster_representatives(2, 0, samples, -105, "Cluster" )
		#clusters=BSCv2.cluster2(2, 0.1, samples, -105, "Cluster" )

		timeCL += time.time() - time1


		lc =[]
		for i in samples2:
			#print("-"*23)
			clusters_merge=[]
			
			time1 = time.time()
			samples_in_cluster=BSCv2.cluster_identification_using_N_APS(i,clusters, N, -73)
			timeCI += time.time() - time1

			lc.append(len(samples_in_cluster))


			if (len(samples_in_cluster)>0):

				time1 = time.time()
				result = KNN3(i, samples_in_cluster, 12)
				
				timeBSCv2 += time.time() - time1

				#print("-"*23)

				BSCv2predict_x.append(result[0])

				BSCv2predict_y.append(result[1])
			else:
				time1 = time.time()
				result = KNN3(i, clF, 12)
				
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