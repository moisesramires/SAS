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

def KNN5(sa,clusters,k):
	distances=[]
	samp=[]
	samples_used=[]
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
		training_rssi.append(samples[j[1]])
		fet_dist.append(j[0])
		#print(j[1])
		Lat += float(dataset[j[1]][0])
		Lon += float(dataset[j[1]][1])
		floor.append(float(dataset[j[1]][2]))
		samples_used.append(j[1])
		#sp.append([j[1]])
	#SS.append(sp)
	f = Counter(floor)
	#print(building)
	#print(b.most_common(1))
	#return ((Lon/k),(Lat/k), int(dataset[distances[0][1]][2]), int(dataset[distances[0][1]][3]) )
	return ((Lon/k),(Lat/k), f.most_common(1)[0][0],samples_used)



print("*"*70)
print("-"*50)
print("\n")
print("Beginnning data parsing and manipulation")
print("\n")

#TUT6  -95  7 0 1
#_no_bellow_treshold
samples = []
dataset = []
with open('../../../SAS_library/datasets/tut6/TUT6_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../../SAS_library/datasets/tut6/TUT6_trncrd_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset.append(row) # samples RSSI
		
#print(dataset[53])
samples2 = []
dataset2 = []
with open('../../../SAS_library/datasets/tut6/TUT6_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../../SAS_library/datasets/tut6/TUT6_tstcrd_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset2.append(row) # samples RSS


true_x = [] # Lat
true_y = [] # Long
true_f = [] # Long


for i in range(0,len(samples2)):
	#print(dataset2[i])
	true_x.append(float(dataset2[i][1]))
	true_y.append(float(dataset2[i][0]))
	true_f.append(float(dataset2[i][2])) # 2 UJI, 4 SAH1

	#break















#clusters =BSCv2.remove_geomtricDistant_samples(dataset, clusters)


#exit()

#UJI

true_x = [] # Lat
true_y = [] # Long
true_f = [] # Floor


for i in range(0,len(samples2)):

	true_x.append(float(dataset2[i][1]))
	true_y.append(float(dataset2[i][0]))
	true_f.append(float(dataset2[i][2])) # 2UJI 4 sah1
	#break



writer = csv.writer(open('tut6_samples_used.csv', 'a', newline=''), delimiter = ";")
writer.writerow(["Testing","Testing RSSI" ,"Estimated", "True", "Error", "Training", "Training RSSI", "Feature distance", "cluster"])

#UJI
for Ts in [-5]:
	BSCv2predict_x = [] # Lat
	BSCv2predict_y = [] # Long
	BSCv2predict_f = [] # Floor
	BSCv2predict_u = [] # Used
	timeBSCv2 = 0
	timeCI = 0

	timeCL=0
	time1 = time.time()
	clusters=BSCv2.clusters=BSCv2.cluster(1, Ts, samples, -95, -30 )
	#clusters=BSCv2.cluster_recalculate_cluster_representatives(2, 0, samples, -105, "Cluster" )
	#clusters=BSCv2.cluster2(2, 0.1, samples, -105, "Cluster" )

	timeCL += time.time() - time1


	lc =[]
	used_cluster = []
	testing_rssi = []
	training_rssi = []
	fet_dist = []
	for i in samples2:
		#print("-"*23)
		clusters_merge=[]
		
		time1 = time.time()
		samples_in_cluster=BSCv2.cluster_identification_using_N_APS(i,clusters, 6, -95)
		timeCI += time.time() - time1

		used_cluster.append(samples_in_cluster)

		testing_rssi.append(i)

		time1 = time.time()
		result = KNN5(i, samples_in_cluster, 1)
		
		timeBSCv2 += time.time() - time1

		#print("-"*23)

		BSCv2predict_x.append(result[0])

		BSCv2predict_y.append(result[1])

		BSCv2predict_f.append(float(result[2]))

		BSCv2predict_u.append(result[3])







	#print(sum(lc)/len(lc))
	#EuclideanDistanceF = []
	EuclideanDistanceBSCv2 = []
	#Fcomp = []
	#BSCv2comp = []
	for k in range(0,len(true_y)):
		bF = np.array((true_x[k], true_y[k],  true_f[k])).astype(float)
		aBSCv2 = np.array((BSCv2predict_x[k], BSCv2predict_y[k],BSCv2predict_f[k])).astype(float)


		
		EuclideanDistanceBSCv2.append(np.linalg.norm(aBSCv2 -bF))

		row=[str(k),testing_rssi[k],str(aBSCv2), str(bF), str(np.linalg.norm(aBSCv2 -bF)), str(BSCv2predict_u[k]), training_rssi[k],fet_dist[k], used_cluster[k]  ]
		writer.writerow(row)

