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


print("-"*50)
print("\n")
print("Beginnning clustering")
print("\n")

#SAH1  -95 4
#_no_bellow_treshold
samples = []
dataset = []
with open('../../../SAS_library/datasets3d/sah1/SAH1_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../../SAS_library/datasets3d/sah1/SAH1_trncrd_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset.append(row) # samples RSSI
		
#print(dataset[53])
samples2 = []
dataset2 = []
with open('../../../SAS_library/datasets3d/sah1/SAH1_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../../SAS_library/datasets3d/sah1/SAH1_tstcrd_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
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

print("-"*50)
print("\n")
print("Beginnning cluster identification and Position estimation")
print("\n")

writer = csv.writer(open('CDF_BSC.csv', 'a', newline=''), delimiter = ";")
#writer.writerow(["N", "Ts", "Median", "Average", "Minimum", "Maximum","Standard Deviation", "KNN Time", "CI Time", "N#C", "Clustering Time"])

# 1 9
clF = range(0,len(samples))
for Ts in [-7]:
	for N in range(1,2):
		BSCpredict_x = [] # Lat
		BSCpredict_y = [] # Long
		BSCpredict_f = [] # Floor
		timeBSC = 0
		time1 = time.time()
		clusters=BSCv2.cluster(1, Ts, samples, -101, -9 )
		timeCL = time.time() - time1
		
		BSCpredict_x = [] # Lat
		BSCpredict_y = [] # Long
		timeBSC = 0

		timeCI = 0
		for i in samples2:
			#print("-"*23)
			clusters_merge=[]
			
			
			time1 = time.time()

			#samples_in_cluster=BSC.cluster_identification2(i,clusters,samples, 6,-73)
			samples_in_cluster=BSCv2.cluster_identification_using_N_APS(i,clusters, N,-95)
			#samples_in_cluster=BSC.cluster_identification_repetition(i,clusters, 6,-73)
			


			timeCI += time.time() - time1

			if (len(samples_in_cluster)>0):
				time1 = time.time()


				result = KNN5(i, samples_in_cluster, 4)
				#result = BSC_SVM(i,samples_in_cluster)
				#result = BSC_BNB(i,samples_in_cluster)
				#print(result)
				timeBSC += time.time() - time1

				#print("-"*23)

				BSCpredict_x.append(result[0])

				BSCpredict_y.append(result[1])

				BSCpredict_f.append(float(result[2]))
				#break
			else:
				time1 = time.time()


				result = KNN5(i, clF, 4)
				#result = BSC_SVM(i,samples_in_cluster)
				#result = BSC_BNB(i,samples_in_cluster)
				#print(result)
				timeBSC += time.time() - time1

				#print("-"*23)

				BSCpredict_x.append(result[0])

				BSCpredict_y.append(result[1])

				BSCpredict_f.append(float(result[2]))
				#break






		#EuclideanDistanceF = []
		EuclideanDistanceBSC = []
			#BSCcomp = []
		for k in range(0,len(true_y)):
			bF = np.array((true_x[k], true_y[k], true_f[k])).astype(float)
			aBSC = np.array((BSCpredict_x[k], BSCpredict_y[k], BSCpredict_f[k])).astype(float)


			
			EuclideanDistanceBSC.append(np.linalg.norm(aBSC -bF))

		#print(BSCpredict_x)
		#print(true_x)
		#print(BSCpredict_y)
		#print(true_y)
		# Statistic values
		print("BSC :")
		print(N)
		

		print ("\t BSC Median: " + str(statistics.median(EuclideanDistanceBSC)) )

		print ("\t BSC Average: " + str(sum(EuclideanDistanceBSC) / len(EuclideanDistanceBSC)) )


		print("\t Time: " + str(timeBSC))
		minimum=np.amin(EuclideanDistanceBSC)
		print("\t BSC Minimum value: " + str(minimum) )
		print("\t BSC Maximum value: " + str(np.amax(EuclideanDistanceBSC) ) )

		print("\t BSC Standard Deviation: " + str(np.std(EuclideanDistanceBSC)))

		print("\t BSC 25th percentile: ",
		       np.percentile(EuclideanDistanceBSC, 25))
		print("\t BSC 50th percentile: ",
		       np.percentile(EuclideanDistanceBSC, 50))
		print("\t BSC 75th percentile: ",
		       np.percentile(EuclideanDistanceBSC, 75))


	


		print("\n")
		print("*"*70)
		print("-"*50)
		print("\n")



		row=[str(N), str(Ts),  str(sum(EuclideanDistanceBSC) / len(EuclideanDistanceBSC))]

		writer.writerow(row)

		for e in range(0,len(EuclideanDistanceBSC)):
			row=[str(EuclideanDistanceBSC[e])]
			writer.writerow(row)