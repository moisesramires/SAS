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

def KNNG(rssi, coordinates ,clusters,k,w ):
	distances=[]
	samp=[]
	s = np.array(rssi).astype(float)
	for i in range(0,len(clusters)):
		samp= np.array(samples[clusters[i]]).astype(float)
		Fdist = np.linalg.norm(s-samp)
		#dist = advanced_Euc(s,samp)

		bF = np.array((dataset[clusters[i]][0], dataset[clusters[i]][1],  dataset[clusters[i]][2])).astype(float)
		aBSCv2 = np.array((coordinates[0], coordinates[1], coordinates[2])).astype(float)			
		Gdist = np.linalg.norm(aBSCv2 -bF)


		distances.append((Gdist, Fdist, clusters[i]))
	#print(distances[0])
	distances.sort(key=lambda x: x[0])
	#print("""""""""""")
	#print(cl)
	#sp = []
	print(len(distances))
	k = min(len(distances),k)
	floor = []
	for j in distances[0:k]:
		#print(j[1])
		row = ["training", str(j[2]), samples[j[2]], dataset[j[2]], j[0], j[1]]
		w.writerow(row)



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









for i in range(0,len(dataset)):
	dataset[i] = [float(j) for j in dataset[i]]
	samples[i] = [float(j) for j in samples[i]]



clF = range(0,len(samples))

#create array with testing sample
array=[6805, 3662]

#iterate the array
for testing_sample in array:

	#get the sample info
	writer = csv.writer(open(str(testing_sample) + '_tut6_samples_used.csv', 'a', newline=''), delimiter = ";")
	writer.writerow(["Type","ID","RSSI" ,"Position", "Geo Distance", "Feat Distance"])
	row = ["Testing",str(testing_sample), samples2[testing_sample],dataset2[testing_sample], "0", "0"]
	writer.writerow(row)
	KNNG(samples2[testing_sample], dataset2[testing_sample],  clF, 5, writer)



	#calculate the K closest samples geometrically

	#save the K closest samples, save info

