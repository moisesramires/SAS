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
	k = min(len(distances),k)
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






print("*"*70)
print("-"*50)
print("\n")
print("Beginnning data parsing and manipulation")
print("\n")




#LIB1 -100 8 4 11

samples = []
dataset = []

#LIB1_trnrss_no_unDetected_no_bellow_treshold
with open('../../../SAS_library/datasets3d/lib1/LIB1_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		
#LIB1_trncrd
with open('../../../SAS_library/datasets3d/lib1/LIB1_trncrd3d.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset.append(row[:3]) # samples RSSI
		
print("-"*50)
print("\n")
print("Beginnning clustering")
print("\n")


#LIB1 

samples2 = []
dataset2 = []
#LIB1_tstrss_no_unDetected_no_bellow_treshold
with open('../../../SAS_library/datasets3d/lib1/LIB1_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		
#LIB1_tstcrd
with open('../../../SAS_library/datasets3d/lib1/LIB1_tstcrd3d.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset2.append(row[:3]) # samples RSSI



#UJI

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

writer = csv.writer(open('lib1.csv', 'a', newline=''), delimiter = ";")
#writer.writerow(["N", "Ts", "Median", "Average", "Minimum", "Maximum","Standard Deviation", "KNN Time", "CI Time","N#C", "CL Time"])


#3 0
#4 0
for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i][:4]]
	samples[i] = [int(j) for j in samples[i]]


clF = range(0,len(samples))
# 3 14
for Ts in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
	for N in range(9,11):
	#for P in range(0,N):

		timeCL=0
		time1 = time.time()
		clusters=BSCv2.cluster(1, Ts, samples, -100, -9 )
		timeCL += time.time() - time1
		BSCv2predict_x = [] # Lat
		BSCv2predict_y = [] # Long
		BSCv2predict_f = [] # Floorg
		timeBSCv2 = 0
		timeCI = 0


		for i in samples2:
			#print("-"*23)
			clusters_merge=[]
			time1 = time.time()

			#samples_in_cluster=BSCv2.cluster_identification2(i,clusters,samples, 3)
			samples_in_cluster=BSCv2.cluster_identification_using_N_APS(i,clusters, N,-99)
			#samples_in_cluster=BSCv2.cluster_identification_repetition(i,clusters, 3)
			
			timeCI += time.time() - time1

			if (len(samples_in_cluster)>0):


				
				time1 = time.time()
				result = KNN5(i, samples_in_cluster, 11)
				#result = BSCv2_SVM(i,samples_in_cluster)
				#result = BSCv2_BNB(i,samples_in_cluster)
				#print(result)
				timeBSCv2 += time.time() - time1

				#print("-"*23)

				BSCv2predict_x.append(result[0])

				BSCv2predict_y.append(result[1])


				BSCv2predict_f.append(float(result[2]))
				#break
			else:

				time1 = time.time()
				result = KNN5(i, clF, 11)
				#result = BSCv2_SVM(i,samples_in_cluster)
				#result = BSCv2_BNB(i,samples_in_cluster)
				#print(result)
				timeBSCv2 += time.time() - time1

				#print("-"*23)

				BSCv2predict_x.append(result[0])

				BSCv2predict_y.append(result[1])


				BSCv2predict_f.append(float(result[2]))
				#break

		row =[]




		BSCv2Error=[]
		FError=[]
		Normal = []
		BSCv2sumError = 0

		#EuclideanDistanceF = []
		EuclideanDistanceBSCv2 = []
			#BSCv2comp = []
		for k in range(0,len(true_y)):
			bF = np.array((true_x[k], true_y[k], true_f[k])).astype(float)
			aBSCv2 = np.array((BSCv2predict_x[k], BSCv2predict_y[k], BSCv2predict_f[k])).astype(float)


			
			EuclideanDistanceBSCv2.append(np.linalg.norm(aBSCv2 -bF))

		#print(BSCv2predict_x)
		#print(true_x)
		#print(BSCv2predict_y)
		#print(true_y)
		# Statistic values
		print("BSCv2 :")
		

		print ("\t BSCv2 Median: " + str(statistics.median(EuclideanDistanceBSCv2)) )

		print ("\t BSCv2 Average: " + str(sum(EuclideanDistanceBSCv2) / len(EuclideanDistanceBSCv2)) )


		print("\t Time: " + str(timeBSCv2))
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
