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
with open('../../../SAS_library/3druns/uji/CDF_PLain.csv', newline='') as csvfile:
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

"""
c=0

#sas
with open('../SAS_library/3druns/uji/CDF_SAS.csv', newline='') as csvfile:
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
"""


c=0
tc=[]
#kmeans
with open('CDF_BSC.csv', newline='') as csvfile:
	spamreader = csv.reader(csvfile, delimiter=';', quotechar='|')
	for row in spamreader:
		if c == 1:
			tc.append(float(row[0]))
		else:
			c=1


# sort the data in ascending order
x_tc = np.sort(tc)
  
# get the cdf values of y
y_tc = np.arange(len(tc)) / float(len(tc))


plt.plot(x_plain,y_plain, label="Plain", color="red")

plt.plot(x_tc,y_tc, label="BSC", color="blue")
#plt.plot(x_sas,y_sas, label="SAS", color="green")
plt.xlabel("Error [m]")
plt.ylabel("Probability Values [%]")
plt.title("CDF distribution")
plt.legend()
plt.show()