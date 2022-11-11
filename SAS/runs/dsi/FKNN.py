
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


#DSI -100 10 2 30

samples = []
dataset = []
with open('../../datasets/dsi/DSI1_trnrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples.append(row) # samples RSSI
		

with open('../../datasets/dsi/DSI1_trncrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		dataset.append(row[:2]) # samples RSSI


samples2 = []
dataset2 = []
with open('../../datasets/dsi/DSI1_tstrss_no_unDetected_no_bellow_treshold.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		samples2.append(row) # samples RSSI
		

with open('../../datasets/dsi/DSI1_tstcrd.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
	for row in spamreader:
		dataset2.append(row[:2]) # samples RSSI

#LIB1 -100 8 0.5 11
#LIB2 -100 6 2 24
print("-"*50)
print("\n")
print("Beginnning clustering")
print("\n")













#clusters =SAS.remove_geomtricDistant_samples(dataset, clusters)

#DSI, LIB
#print(len(dataset2))
#print(len(samples2))
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



writer = csv.writer(open('idealFULLK.csv', 'a', newline=''), delimiter = ";")
for knm in range(1,33):
	timeF = 0
	time1 = 0

	true_x = [] # Lat
	true_y = [] # Long
	Fpredict_x = [] # Lat
	Fpredict_y = [] # Long
	clF = range(0,len(samples))
	for m in range(0,len(samples2)):
		true_x.append(float(dataset2[m][1]))
		true_y.append(float(dataset2[m][0]))
		#print(true_x)
		#print(true_y)
	for m in range(0,len(samples2)):
		time1 = time.time()
		result = KNN2(samples2[m], clF, knm)
		timeF += time.time() - time1
		Fpredict_x.append(result[0])

		Fpredict_y.append(result[1])

	
	FError=[]
	Normal = []
	FsumError = 0
	EuclideanDistanceF = []
	alld=[]
	#print(true_b[-10])
	#print(Fpredict_b[-10])
	for k in range(0,len(true_y)):
		bF = np.array((true_x[k], true_y[k])).astype(float)
		aF = np.array((Fpredict_x[k], Fpredict_y[k])).astype(float)
		EuclideanDistanceF.append(np.linalg.norm(aF -bF))


	print("F :")
	print(knm)
	
	
	
	print ("\t F Median: " + str(statistics.median(EuclideanDistanceF)) )

	print ("\t F Average: " + str(sum(EuclideanDistanceF) / len(EuclideanDistanceF)) )


	minimumF=np.amin(EuclideanDistanceF)
	print("\t F Minimum value: " + str(minimumF) )
	print("\t F Maximum value: " + str(np.amax(EuclideanDistanceF) ) )

	print("\t F Standard Deviation: " + str(np.std(EuclideanDistanceF)))

	print("\t F 25th percentile: ",
	       np.percentile(EuclideanDistanceF, 25))
	print("\t F 50th percentile: ",
	       np.percentile(EuclideanDistanceF, 50))
	print("\t F 75th percentile: ",
	       np.percentile(EuclideanDistanceF, 75))

	print("\t F Time: " + str(timeF))

	

	print("\n")
	print("*"*70)
	print("-"*50)
	print("\n")

	row=[str(knm),str(statistics.median(EuclideanDistanceF)), str(sum(EuclideanDistanceF) / len(EuclideanDistanceF)), str(minimumF),  str(np.amax(EuclideanDistanceF) ),  str(np.std(EuclideanDistanceF)), str(timeF)]
	writer.writerow(row)

	#print(alld)

