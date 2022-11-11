import time

import statistics
import matplotlib.pyplot as plt
import csv
import sys
import numpy as np
import plotly.graph_objects as go
import statistics
from collections import Counter
import json
import sys





"""
 ### AP1  AP2  AP3  ...  APN
 max_  []   []   []   ...  []
-31  ...
-32
 ...
 min_
"""

"""
cluster : 
{
	AP1 : 
	{
		-30 : [s1,s5,s7,s91, ...]
		-31 : [s5,s91,s203, ...]
		-32 : ...
		 ...
		-105 : [s9871, s19201, ...]
	}
	AP2 :
	...
	
}

	N bigger than 1 to many clusters
	(400!)/(2!(400-2)!) * 75 
"""

# ----------------------------------------------------CLUSTERING----------------------------------------------------

def cluster(N, Treshold, samples, undetected,  max_):

	N = N * -1
	
	# The first step is to take the N strongest APs from each sample, aand the highest RSSI
	
	strongestAPs_matrix = [] # the array with the strongest APs for each sample
	strongestRSSI_matrix = [] # the array with the Strongests RSSI for each sample
	number_of_Aps = len(samples[0])


	orded_samples = samples.copy()
	# Get the Nnth strongest APs and RSSI for each sample
	for i in range(0,len(samples)):
		orded_samples[i] = [float(j) for j in orded_samples[i]]
		samples[i] = [float(j) for j in samples[i]]
		orded_samples[i].sort()# Sort the RSSI in a sample
		sample = []
		validAPs = 0
		#print(orded_samples[i])
		# iterate the N strongest RSSIs

		for k in orded_samples[i][N:]:
			
			# the RSSI was undetected
			if k <= float(undetected):
				sample.append(-1)		

			# th RSSI was detected
			else:
				ind=0
				# find the AP with the corresponding RSSI
				while samples[i].index(k,ind) in sample:
					ind += 1
				sample.append(samples[i].index(k,ind))

				validAPs +=1

		# dont add the samples that dont have enough detected APs
		if validAPs >= ((-1*N)):
			sample.append(float(orded_samples[i][-1:][0])) #Order by strongest RSSI
			sample.append(i)
			strongestAPs_matrix.append(sample)
		

	added_samples=[]
	clusters = {}
	#no cluster representatives

	# for in samples:
		# for cl in rssi+treshold .. rssi-treshold:
			# cluster[AP][cl].add(sample)





	# iterate the samples strongests APs
	for s in range(0,len(strongestAPs_matrix)):
		for c in range (int(strongestAPs_matrix[s][-2]) + Treshold, int(strongestAPs_matrix[s][-2]) - Treshold + 1):
			if( strongestAPs_matrix[s][0] not in clusters):
				clusters[strongestAPs_matrix[s][0]] = {}
			if( c not in clusters[strongestAPs_matrix[s][0]]):
				clusters[strongestAPs_matrix[s][0]][c]= []
			clusters[strongestAPs_matrix[s][0]][c].append(strongestAPs_matrix[s][-1])


	

	# save the clusters to a json file
	with open("clusters.json", 'w') as outfile:
		json.dump(clusters, outfile, indent=4)
	
	print("1-*"*10)
	return(clusters)


def cluster_identification(input_sample,clusters, N, min_):
	
	N = N*-1
	sample = input_sample.copy()
	sample = [float(j) for j in sample]
	input_sample = [float(j) for j in input_sample]
	
	sample.sort()
	sample2 = []
	k = sample[N]
	ind = 0
	if k != min_:
		while input_sample.index(k,ind) in sample2:
			ind += 1
		while input_sample.index(k,ind) not in clusters:
			N -= 1
			k = sample[N]

		


	w = k
	print(k)
	print(input_sample.index(w,ind))

	while k not in clusters[input_sample.index(w,ind)]:
		if k > -105:
			k -= 1
			print("--> " + str(k))
		else:
			break

	if  k not in clusters[input_sample.index(w,ind)]:
		k=w
		while k not in clusters[input_sample.index(w,ind)]:
			if k < -30:
				k += 1
				print("--> " + str(k))
			else:
				break





	
	#print (len(list(dict.fromkeys(clusters_merge))))	
	return list(dict.fromkeys(clusters[input_sample.index(w,ind)][k]))