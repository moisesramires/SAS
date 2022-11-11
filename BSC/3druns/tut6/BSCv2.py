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
		final_sample=[]
		for j in range(0,len(samples[i])):
			final_sample.append((j,samples[i][j]))




		sorter = lambda x: (x[1])
		sorted_final_sample = sorted(final_sample, key=sorter)
		for k in sorted_final_sample[N:]:
			
			# the RSSI was undetected
			if k[1] <= float(undetected):
				sample.append(-1)		

			# th RSSI was detected
			else:				
				sample.append(k[0])

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



	count=0
	# iterate the samples strongests APs
	for s in range(0,len(strongestAPs_matrix)):
		print(count)
		count+=1
		for c in range (int(strongestAPs_matrix[s][-2]) + Treshold, int(strongestAPs_matrix[s][-2]) - Treshold + 1):
			if( strongestAPs_matrix[s][0] not in clusters):
				clusters[strongestAPs_matrix[s][0]] = {}
			if( c not in clusters[strongestAPs_matrix[s][0]]):
				clusters[strongestAPs_matrix[s][0]][c]= []
			clusters[strongestAPs_matrix[s][0]][c].append(strongestAPs_matrix[s][-1])
			for i in range(0,len(samples)):
				if( i not in clusters[strongestAPs_matrix[s][0]][c]):
					#print(samples[i][strongestAPs_matrix[s][0]] )
					if( samples[i][strongestAPs_matrix[s][0]] >= int(c) + Treshold and samples[i][strongestAPs_matrix[s][0]] <= int(c) - Treshold):

						clusters[strongestAPs_matrix[s][0]][c].append(i)


	

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
	k = sample[N]
	ind = 0
	if k != min_:
		while input_sample.index(k,ind) not in clusters:
			N -= 1
			k = sample[N]

		


	w = k
	print(k)
	print(input_sample.index(w,ind))

	while k not in clusters[input_sample.index(w,ind)]:
		if k < -9:
			k += 1
			print("--> " + str(k))
		else:
			break

	if  k not in clusters[input_sample.index(w,ind)]:
		k=w
		while k not in clusters[input_sample.index(w,ind)]:
			if k > -105:
				k -= 1
				print("--> " + str(k))
			else:
				break





	try:
	#print (len(list(dict.fromkeys(clusters_merge))))	
		return list(dict.fromkeys(clusters[input_sample.index(w,ind)][k]))
	except:
		return list([])




def cluster_identification_using_N_APS(input_sample,clusters, N, min_):
	current=0
	sample = input_sample.copy()
	sample = [float(j) for j in sample]
	input_sample = [float(j) for j in input_sample]
	samples_in_cluster=[]
	sample.sort()
	final_sample=[]
	for i in range(0,len(input_sample)):
		final_sample.append((i,input_sample[i]))



	sorter = lambda x: (x[1])
	sorted_final_sample = sorted(final_sample, key=sorter)
	sorted_final_sample.reverse()



	for count in range(0,N):
	
		try:
			rssi = sorted_final_sample[count][1]
			id_ = sorted_final_sample[count][0]
			


			w = rssi

			while rssi not in clusters[id_]:
				if rssi < -9:
					rssi += 1
				else:
					break

			if  rssi not in clusters[id_]:
				rssi=w
				while rssi not in clusters[id_]:
					if rssi > -105:
						rssi -= 1
					else:
						break
			samples_in_cluster+=list(dict.fromkeys(clusters[id_][rssi]))
			
		except:
			pass
	return list(dict.fromkeys(samples_in_cluster))	
