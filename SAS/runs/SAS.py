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

#from sklearn.neighbors.nearest_centroid import NearestCentroid
from sklearn.neighbors import NearestCentroid
"""


What does SAS do?

	1. Cluster the radiomap, save the clusters and the clusters representatives.   OFFLINE PHASE
	2. Identify an incoming sample cluster.   ONLINE PHASE



What does SAS need?
	N, the umber of strongest APs to take
	P, the percentage of similarity
	Samples, the samples to cluster, a set of float arrays that represent the RSSI collected
	undetected, the value that represents and undetected RSSI, if there are no undetected RSSI set it to 1
	fileName, the file to save the JSON CLusters



What can SAS offer?
	The offline phase maybe heavier, but the online phase can become a lot lighter in terms of processing cost
"""



# ----------------------------------------------------CLUSTERING----------------------------------------------------

def cluster(N, P, samples, undetected, fileName):

	N = N * -1
	
	# The first step is to take the N strongest APs from each sample, aand the highest RSSI
	
	strongestAPs_matrix = [] # the array with the strongest APs for each sample
	strongestRSSI_matrix = [] # the array with the Strongests RSSI for each sample



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
		if validAPs > ((-1*N*P)):
			sample.append(float(orded_samples[i][-1:][0])) #Order by strongest RSSI
			sample.append(i)
			strongestAPs_matrix.append(sample)
		






	#sort the collected data by each sample strongest RSSI 
	sorter = lambda x: (x[-2])
	sorted_strongestAPs_matrix = sorted(strongestAPs_matrix, key=sorter)
	sorted_strongestAPs_matrix.reverse()

	added_samples=[]
	clusters = {}
	cluster_representative =[]
	count = 0
	marked = set()
	labels=[-1] * len(sorted_strongestAPs_matrix)

	# iterate the samples strongests APs
	for s in range(0,len(sorted_strongestAPs_matrix)):
		# sample isnt part of a cluster, so it can be a cluster representative, and fomr itsown cluster
		if sorted_strongestAPs_matrix[s][-1] not in marked:
			cluster = []
			cluster_representative.append(sorted_strongestAPs_matrix[s])
			cluster_name= "Cluster" + str(count)
			for ss in range(0,len(strongestAPs_matrix)):
				similar = 0
				if sorted_strongestAPs_matrix[s] == strongestAPs_matrix[ss]:
					cluster.append(ss)
					labels[ss]=count
					marked.add(sorted_strongestAPs_matrix[s][-1])
				else:
					for ap in strongestAPs_matrix[ss][:-2]:
						if ap in sorted_strongestAPs_matrix[s] and ap != -1:
							similar += 1
					if similar > (-P*N ):
						cluster.append(ss)
						labels[ss]=count
						marked.add(strongestAPs_matrix[ss][-1])
			
							
			clusters[cluster_name] = cluster
			count += 1

	
	clusters["Cluster_Representatives"] = cluster_representative

	# save the clusters to a json file
	with open(fileName+".json", 'w') as outfile:
		json.dump(clusters, outfile, indent=4)

	return(clusters)



def cluster2(N, P, samples, undetected, fileName):

	N = N * -1
	
	# The first step is to take the N strongest APs from each sample, aand the highest RSSI
	
	strongestAPs_matrix = [] # the array with the strongest APs for each sample
	strongestRSSI_matrix = [] # the array with the Strongests RSSI for each sample



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
		if validAPs > ((-1*N*P)):
			sample.append(float(orded_samples[i][-1:][0])) #Order by strongest RSSI
			sample.append(i)
			strongestAPs_matrix.append(sample)
		






	#sort the collected data by each sample strongest RSSI 
	sorter = lambda x: (x[-2])
	sorted_strongestAPs_matrix = sorted(strongestAPs_matrix, key=sorter)
	sorted_strongestAPs_matrix.reverse()

	added_samples=[]
	clusters = {}
	cluster_representative =[]
	count = 0
	marked = set()
	labels=[-1] * len(sorted_strongestAPs_matrix)
	x = []
	y = []
	# iterate the samples strongests APs
	for s in range(0,len(sorted_strongestAPs_matrix)):
		# sample isnt part of a cluster, so it can be a cluster representative, and fomr itsown cluster
		if sorted_strongestAPs_matrix[s][-1] not in marked:
			cluster = []
			cluster_representative.append(sorted_strongestAPs_matrix[s])
			cluster_name= "Cluster" + str(count)
			for ss in range(0,len(strongestAPs_matrix)):
				similar = 0
				if sorted_strongestAPs_matrix[s] == strongestAPs_matrix[ss]:
					cluster.append(ss)
					x.append(np.array(samples[ss]).astype(int))
					y.append(count)
					labels[ss]=count
					marked.add(sorted_strongestAPs_matrix[s][-1])
				else:
					for ap in strongestAPs_matrix[ss][:-2]:
						if ap in sorted_strongestAPs_matrix[s] and ap != -1:
							similar += 1
					if similar > (-P*N ):
						cluster.append(ss)
						labels[ss]=count
						x.append(np.array(samples[ss]).astype(int))
						y.append(count)
						marked.add(strongestAPs_matrix[ss][-1])
			
							
			clusters[cluster_name] = cluster
			count += 1

	x = np.array(x)
	y = np.array(y)
	clf = NearestCentroid()
	clf.fit(x, y)

	print(clf.centroids_)
	
	clusters["Cluster_Representatives"] = cluster_representative
	clusters["Cluster_Centroids"]  = clf.centroids_.tolist()
	# save the clusters to a json file
	with open(fileName+".json", 'w') as outfile:
		json.dump(clusters, outfile, indent=4)

	return(clusters)



def cluster_int(N, P, samples, undetected, fileName):

	N = N * -1
	
	# The first step is to take the N strongest APs from each sample, aand the highest RSSI
	
	strongestAPs_matrix = [] # the array with the strongest APs for each sample
	strongestRSSI_matrix = [] # the array with the Strongests RSSI for each sample



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
		if validAPs > ((P)):
			sample.append(float(orded_samples[i][-1:][0])) #Order by strongest RSSI
			sample.append(i)
			strongestAPs_matrix.append(sample)
		






	#sort the collected data by each sample strongest RSSI 
	sorter = lambda x: (x[-2])
	sorted_strongestAPs_matrix = sorted(strongestAPs_matrix, key=sorter)
	sorted_strongestAPs_matrix.reverse()

	added_samples=[]
	clusters = {}
	cluster_representative =[]
	count = 0
	marked = set()
	labels=[-1] * len(sorted_strongestAPs_matrix)

	# iterate the samples strongests APs
	for s in range(0,len(sorted_strongestAPs_matrix)):
		# sample isnt part of a cluster, so it can be a cluster representative, and fomr itsown cluster
		if sorted_strongestAPs_matrix[s][-1] not in marked:
			cluster = []
			cluster_representative.append(sorted_strongestAPs_matrix[s])
			cluster_name= "Cluster" + str(count)
			for ss in range(0,len(strongestAPs_matrix)):
				similar = 0
				if sorted_strongestAPs_matrix[s] == strongestAPs_matrix[ss]:
					cluster.append(ss)
					labels[ss]=count
					marked.add(sorted_strongestAPs_matrix[s][-1])
				else:
					for ap in strongestAPs_matrix[ss][:-2]:
						if ap in sorted_strongestAPs_matrix[s] and ap != -1:
							similar += 1
					if similar > (P ):
						cluster.append(ss)
						labels[ss]=count
						marked.add(strongestAPs_matrix[ss][-1])
			
							
			clusters[cluster_name] = cluster
			count += 1

	
	clusters["Cluster_Representatives"] = cluster_representative

	# save the clusters to a json file
	with open(fileName+".json", 'w') as outfile:
		json.dump(clusters, outfile, indent=4)

	return(clusters)







# ----------------------------------------------------CLUSTER CLEAN UP----------------------------------------------------

def remove_geomtricDistant_samples(coordinates, clusters):

	clusters_final= {}
	#clusters_final["Cluster_Representatives"] = clusters["Cluster_Representatives"]
	cp = []
	c = -1
	w = 0
	
	for i in clusters:
		cdr_arr=[]
		c+=1
		repre=[]
		la=[]
		lo=[]
		
		if i != "Cluster_Representatives":
			
			#print(clusters["Cluster_Representatives"][c][-1])
			for j in clusters[i]:
				la.append(float(coordinates[j][0]))
				lo.append(float(coordinates[j][1]))
			repre.append(sum(la)/len(la))
			repre.append(sum(lo)/len(lo))
			repre = np.array(repre).astype(float)
			for j in clusters[i]:
				cdr=[]
				cdr.append(float(coordinates[j][0]))
				cdr.append(float(coordinates[j][1]))
				cdr = np.array(cdr).astype(float)
				
				cdr_arr.append(np.linalg.norm(  repre - cdr ))
			new_clt = []
			#print(np.std(cdr_arr))
			for k in range(0,len(cdr_arr)):
				#print(cdr_arr[k])
				# 2.5
				if abs(cdr_arr[k]) < abs(np.std(cdr_arr)*2.5): #(abs((sum(cdr_arr)/len(cdr_arr))) + abs(np.std(cdr_arr))):
					new_clt.append(clusters[i][k])
			if len(new_clt) > 0:

				name = "Cluster" + str(w)
				w+=1
				clusters_final[name]=new_clt
				cp.append(clusters["Cluster_Representatives"][c])
				if(len(new_clt)<len( clusters[i])):
					print("New: " + str(len(new_clt)) + "   Original: "  +str(len( clusters[i])))
	clusters_final["Cluster_Representatives"] = cp

	return clusters_final










# ----------------------------------------------------CLUSTER IDENTIFICATION----------------------------------------------------
def cluster_identification(input_sample,clusters, N, min_):
	labels=[]
	N = N*-1
	sample = input_sample.copy()
	sample = [float(j) for j in sample]
	input_sample = [float(j) for j in input_sample]
	
	sample.sort()
	sample2 = []
	for k in sample[N:]:
		ind=0
		if k != min_:
			while input_sample.index(k,ind) in sample2:
				ind += 1
			sample2.append(input_sample.index(k,ind))
		else:
			sample2.append(-2)

	

	clusters_merge=[]
	max_ = 0
	c =0
	for i in clusters["Cluster_Representatives"]:
		similar= 0
		for ap in sample2:
			if ap in i[:-2]:
				similar += 1
		if similar > max_:
			max_= similar
			clusters_merge=clusters["Cluster"+str(c)].copy()
		elif similar== max_:
			#print(clusters_merge)
			clusters_merge+=clusters["Cluster"+str(c)].copy()
			#print(clusters_merge)
		c+=1
	
		
	#print (len(list(dict.fromkeys(clusters_merge))))	
	return list(dict.fromkeys(clusters_merge))

def cluster_identification_repetition(input_sample,clusters, N, min_):
	labels=[]
	N = N*-1
	sample = input_sample.copy()
	sample = [float(j) for j in sample]
	input_sample = [float(j) for j in input_sample]
	
	sample.sort()
	sample2 = []
	for k in sample[N:]:
		ind=0
		if k != min_:
			while input_sample.index(k,ind) in sample2:
				ind += 1
			sample2.append(input_sample.index(k,ind))
		else:
			sample2.append(-2)

	

	clusters_merge=[]
	max_ = 0
	c =0
	for i in clusters["Cluster_Representatives"]:
		similar= 0
		for ap in sample2:
			if ap in i[:-2]:
				similar += 1
		if similar > max_:
			max_= similar
			clusters_merge=clusters["Cluster"+str(c)].copy()
		elif similar== max_:
			clusters_merge+=clusters["Cluster"+str(c)].copy()
		c+=1
	
		

	return clusters_merge
def cluster_identification2(input_sample,clusters,samples, N):
	labels=[]
	N = N*-1
	sample = input_sample.copy()
	sample = [float(j) for j in sample]
	input_sample = [float(j) for j in input_sample]
	

	

	clusters_merge=[]
	max_ = []
	m=0
	c =0
	ind =0

	s = np.array(input_sample).astype(int)
	for i in clusters["Cluster_Centroids"]:

		samp = np.array(i).astype(int)
		if m == 0:
			m =np.linalg.norm(s-samp)
			ind = 0 
		else:
			similar=  np.linalg.norm(s-samp)	
			if similar < m :
				ind = c
				m = similar	
			max_.append(similar)
		c+=1
	#print (max_)
	#print(ind)
	clusters_merge=clusters["Cluster"+str(ind)].copy()
	return clusters_merge



def cluster_identification3(input_sample,clusters,samples, N):
	labels=[]
	N = N*-1
	sample = input_sample.copy()
	sample = [float(j) for j in sample]
	input_sample = [float(j) for j in input_sample]
	

	

	clusters_merge=[]
	max_ = []
	m=0
	c =0
	ind =0

	s = np.array(input_sample).astype(int)
	for i in clusters["Cluster_Representatives"]:

		samp = np.array(samples[i[-1]]).astype(int)
		if m == 0:
			m =np.linalg.norm(s-samp)
			ind = 0 
		else:
			similar=  np.linalg.norm(s-samp)	
			if similar < m :
				ind = c
				m = similar	
			max_.append(similar)
		c+=1
	#print (max_)
	#print(ind)
	clusters_merge=clusters["Cluster"+str(ind)].copy()
	return clusters_merge