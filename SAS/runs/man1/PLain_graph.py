
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
with open('idealFULLK.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
    for row in spamreader:
        cluster_intersection.append(row)

print(cluster_intersection[0])


k=[]
avg=[]
time=[]
for i in cluster_intersection:
	k.append(float(i[0]))
	avg.append(float(i[2]))
	time.append(float(i[6])/460*1000)
	




print(k[0])
print(avg[0])
print(time[0])


fig, axs = plt.subplots(1, 2)

axs[0].plot(k, time)
#axs[1].set(ylabel='Average error',fontsize=12)
axs[0].set_ylabel('Matching Time',fontsize=12)
axs[0].set_xlabel('k',fontsize=11)


axs[0].tick_params(labelsize=12)




axs[1].plot(k,avg)
axs[1].set_ylabel('APE [m]',fontsize=12)

axs[1].set_xlabel('k',fontsize=11)

axs[1].tick_params(labelsize=12)





#Comment to get (N,P)
#axs[1,1].set_xticks([])


#plt.locator_params(axis='x', nbins=10)
plt.legend()
plt.show()