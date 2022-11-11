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



sas = []
plain = []
c=0
#trainingdata
with open('CDF_PLain.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		if c == 1:
			plain.append(float(row[0]))
		else:
			c=1


# sort the data in ascending order
x_plain = np.sort(plain)
  
# get the cdf values of y
y_plain = np.arange(len(plain)) / float(len(plain))

c=0

#sas
with open('CDF_SAS.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		if c == 1:
			sas.append(float(row[0]))
		else:
			c=1


# sort the data in ascending order
x_sas = np.sort(sas)
  
# get the cdf values of y
y_sas = np.arange(len(sas)) / float(len(sas))



c=0
kmeans=[]
#kmeans
with open('../../../KMEANS/3druns/tut6/CDF_KMEANS.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		if c == 1:
			kmeans.append(float(row[0]))
		else:
			c=1


# sort the data in ascending order
x_kmeans = np.sort(kmeans)
  
# get the cdf values of y
y_kmeans = np.arange(len(kmeans)) / float(len(kmeans))



c=0
bsc=[]
#bsc
with open('../../../BSCv2/3druns/tut6/CDF_BSC.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		if c == 1:
			bsc.append(float(row[0]))
		else:
			c=1


# sort the data in ascending order
x_bsc = np.sort(bsc)
  
# get the cdf values of y
y_bsc = np.arange(len(bsc)) / float(len(bsc))



plt.plot(x_plain,y_plain, label="Plain", color="red")

plt.plot(x_kmeans,y_kmeans, label="$\it{K}$-Means", color="brown")
plt.plot(x_bsc,y_bsc, label="BSC", color="blue")
plt.plot(x_sas,y_sas, label="SAS", color="green")
#plt.plot(cdf_b,label="Bad")
plt.xlabel("Error [m]",fontsize=12)
plt.ylabel("Probability Values [%]",fontsize=12)
plt.title("CDF distribution",fontsize=12)
plt.tick_params(labelsize=12)
plt.legend()
plt.show()