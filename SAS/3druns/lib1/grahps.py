
import matplotlib.pyplot as plt
import time

import csv
import sys
import numpy as np
import plotly.graph_objects as go
import statistics
from sklearn.metrics import calinski_harabasz_score, davies_bouldin_score
from collections import Counter
import json
import sys


seconds = time.time()

np.set_printoptions(threshold=sys.maxsize) # print full array

print("*"*70)
print("-"*50)
print("\n")
print("Beginnning data parsing and manipulation")
print("\n")

cluster_intersection = []
with open('lib1.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        cluster_intersection.append(row)

print(cluster_intersection[0])


#remove the labels row
cluster_intersection.pop(0)
x_dict = {}
x2_dict = {}
x3_dict = {}
x4_dict = {}
N=[]
for i in cluster_intersection:
	if ((int(i[0])*-1) not in N):
		N.append((int(i[0])*-1))
		x_dict[(int(i[0])*-1)]=[]
		x2_dict[(int(i[0])*-1)]=[]
		x3_dict[(int(i[0])*-1)]=[]
		x4_dict[(int(i[0])*-1)]=[]
	#12
	#5
	x_dict[(int(i[0])*-1)].append(float(i[3]))
	x2_dict[(int(i[0])*-1)].append(float(i[7])/576*1000)
	x3_dict[(int(i[0])*-1)].append(float(i[8])/576*1000)
	x4_dict[(int(i[0])*-1)].append(float(i[9]))
	
	






print (x_dict)
fig, axs = plt.subplots(2, 2)
"""axs[1, 0].plot(x, -y, 'tab:green')
axs[1, 0].set_title('Axis [1, 0]')
axs[1, 1].plot(x, -y, 'tab:red')
axs[1, 1].set_title('Axis [1, 1]')
"""
#['red', 'black', 'blue', 'brown', 'green',"c","m"]
w= range(0,N[-1])
e = len(N)
cm = plt.get_cmap('gist_rainbow')
axs[0, 0].set_prop_cycle('color', [cm(1.*i/e) for i in range(e)])
axs[0, 1].set_prop_cycle('color', [cm(1.*i/e) for i in range(e)])
axs[1, 0].set_prop_cycle('color', [cm(1.*i/e) for i in range(e)])
axs[1, 1].set_prop_cycle('color', [cm(1.*i/e) for i in range(e)])
for j in N:

	x1 = range(0,j)
	
	print(x_dict[j])
	axs[0, 1].plot(x1, x_dict[j], label = "N="+ str(j))
	#axs[0, 0].set(ylabel='Average error',fontsize=12)
	axs[0, 1].set_ylabel('APE [m]',fontsize=12)
	axs[0, 1].set_xlabel('P',fontsize=11)

	
	axs[0,1].set_xticks(w)
	axs[0,1].tick_params(labelsize=12)


	axs[1, 1].plot(x1, x2_dict[j], label = "N="+ str(j))
	axs[1, 1].set_ylabel('Matching Time [ms]',fontsize=12)
	axs[1, 1].set_xlabel('P',fontsize=11)

	
	axs[1,1].set_xticks(w)
	axs[1,1].tick_params(labelsize=12)


	axs[1, 0].plot(x1, x3_dict[j], label = "N="+ str(j))
	axs[1, 0].set_ylabel('Cluster Identification Time [ms]',fontsize=12)

	axs[1, 0].set_xlabel('P',fontsize=11)

	
	axs[1,0].set_xticks(w)
	axs[1,0].tick_params(labelsize=12)


	axs[0, 0].plot(x1, x4_dict[j], label = "N="+ str(j))
	axs[0, 0].set_ylabel('N# clusters',fontsize=12)

	axs[0, 0].set_xlabel('P',fontsize=11)
	
	axs[0,0].set_xticks(w)
	axs[0,0].tick_params(labelsize=12)






#Comment to get (N,P)
#axs[1,1].set_xticks([])


#plt.locator_params(axis='x', nbins=10)
plt.legend(loc='lower left', bbox_to_anchor=(1, 0.5))
plt.show()