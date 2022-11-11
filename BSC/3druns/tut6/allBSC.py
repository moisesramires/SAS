

import matplotlib.pyplot as plt
import time

import csv
import sys
import numpy as np
import plotly.graph_objects as go
import statistics
from collections import Counter
import json
import sys


#BSC
BSC_Error = []
BSC_Time = []

#BSCv2
BSCv2_Error = []
BSCv2_Time = []

#BSCv3
BSCv3_Error = []
BSCv3_Time = []


#KMEANS
KMEANS_Error = []
KMEANS_Time = []


#SAS
SAS_Error = []
SAS_Time = []

#Plain
Plain_Error = []
Plain_Time = []



#tut6

#BSC -20
BSC_Error.append(4.0953178287565954)
BSC_Time.append(11.715288877487183+ 1.6575806140899658)


#BSCv2 -1
BSCv2_Error.append(3.7864226424500926)
BSCv2_Time.append(21.3213894367218+ 1.8339459896087646)

#BSCv3 9 -1
BSCv3_Error.append(2.4357830475496858)
BSCv3_Time.append(72.04100584983826+ 3.6355085372924805)

#BSCv3 14 -1
BSCv3_Error.append(2.2994861866088008)
BSCv3_Time.append(97.31094431877136+ 5.241824388504028)



#SAS 9 0
SAS_Error.append(2.049656417701045)
SAS_Time.append(104.45987963676453+ 12.205966711044312)

#KMEANS
KMEANS_Error.append(2.0925495877101397)
KMEANS_Time.append( 575.4805016517639 + 21.227607011795044)



#Plain
Plain_Error.append(2.0784267649449224)
Plain_Time.append(874.4274911880493)









labels=[ "tut6"]

plt.style.use('seaborn-whitegrid')

BSCNE=[]
BSCNT=[]

BSCv2NE=[]
BSCv2NT=[]

BSCv3NE=[]
BSCv3NT=[]

SASNE=[]
SASNT=[]

KMEANSNE=[]
KMEANSNT=[]
c=0
for i in range(0,len(Plain_Error)):
	BSCNE.append(BSC_Error[i]/Plain_Error[i])
	BSCNT.append(BSC_Time[i]/Plain_Time[i])

	BSCv2NE.append(BSCv2_Error[i]/Plain_Error[i])
	BSCv2NT.append(BSCv2_Time[i]/Plain_Time[i])

	BSCv3NE.append(BSCv3_Error[i]/Plain_Error[i])
	BSCv3NT.append(BSCv3_Time[i]/Plain_Time[i])

	SASNE.append(SAS_Error[i]/Plain_Error[i])
	SASNT.append(SAS_Time[i]/Plain_Time[i])

	KMEANSNE.append(KMEANS_Error[i]/Plain_Error[i])

	KMEANSNT.append(KMEANS_Time[i]/Plain_Time[i])
	c+=1
BSCv3NE.append(BSCv3_Error[1]/Plain_Error[0])
BSCv3NT.append(BSCv3_Time[1]/Plain_Time[0])




plt.plot(BSCNE, BSCNT, 'o', color='blue',label="BSC");
plt.plot(BSCv2NE, BSCv2NT, 'o', color='purple',label="BSCv2");
plt.plot(BSCv3NE, BSCv3NT, 'o', color='orange',label="BSCv3");

plt.plot(SASNE, SASNT, 'o', color='green',label="SAS");
plt.plot(KMEANSNE, KMEANSNT, 'o', color='brown',label="KMEANS");
plt.plot([1], [1], 'o', color='red',label="Plain");
plt.xlim(0.7,2.1)
plt.xlabel("Error")
plt.ylabel("Time")
plt.legend()
plt.show()