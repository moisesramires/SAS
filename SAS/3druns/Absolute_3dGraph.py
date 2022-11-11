

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


#SAS
SAS_Error = []
SAS_Time = []


#KMEANS
KMEANS_Error = []
KMEANS_Time = []



#Plain
Plain_Error = []
Plain_Time = []


#size
testing=[]




#lib1

#SAS 8 4
SAS_Error.append(2.36)
SAS_Time.append(6.61505603790283 + 0.1099534034729)


#KMEANS
KMEANS_Error.append(2.3356375822289093)
KMEANS_Time.append(1.6486802101135254 + 0.1750338077545166)



#Plain
Plain_Error.append(2.439044375907644)
Plain_Time.append(27.78903102874756)

#size
testing.append(576)


#lib2



#SAS 6 1
SAS_Error.append(2.78205551577453)
SAS_Time.append(10.4835102558136 + 0.106250047683716)


#KMEANS
KMEANS_Error.append(2.8115578739279865)
KMEANS_Time.append(1.5296635627746582 + 0.1753220558166504 )



#Plain
Plain_Error.append(2.9150480177067597)
Plain_Time.append(26.870366096496582)


#size
testing.append(576)


#sah1

#SAS 4 1
SAS_Error.append(5.866169811694326)
SAS_Time.append(2.9244742393493652 + 0.13327336311340332)


#KMEANS
KMEANS_Error.append(6.042812267703738)
KMEANS_Time.append(22.927672386169434 + 0.08941817283630371)



#Plain
Plain_Error.append(6.250726726257672)
Plain_Time.append(75.26426792144775)

#size
testing.append(156)

#tut5

#SAS 18 0
SAS_Error.append(6.222883374912352)
SAS_Time.append(4.218442916870117 + 0.3137836456298828)


#KMEANS
KMEANS_Error.append(6.4543851236371355)
KMEANS_Time.append(1.2746453285217285 + 0.4122936725616455 )



#Plain
Plain_Error.append(6.253951032064151)
Plain_Time.append(14.877002716064453)

#size
testing.append(975)


#tut6

#SAS 9 0
SAS_Error.append(2.0378911841687284)
SAS_Time.append(112.94274854660034+ 3.4594995975494385)


#KMEANS
KMEANS_Error.append(2.0925495877101397)
KMEANS_Time.append( 575.4805016517639 + 21.227607011795044)



#Plain
Plain_Error.append(2.0784267649449224)
Plain_Time.append(874.4274911880493)


#size
testing.append(7237)




#uji


#SAS 3 0
SAS_Error.append(8.20868403926468)
SAS_Time.append(32.71047401428223 + 0.624464750289917)


#KMEANS
KMEANS_Error.append(8.873737535521615)
KMEANS_Time.append(56.37391257286072 + 0.5578653812408447)



#Plain
Plain_Error.append(8.838846993928243)
Plain_Time.append(680.3997316360474)


#size
testing.append(1111)


#uts1


#SAS 5 1
SAS_Error.append(7.141207308328751)
SAS_Time.append(20.353198528289795 + 0.23497676849365234)


#KMEANS
KMEANS_Error.append(7.410185240687027)
KMEANS_Time.append(7.709730625152588+ 0.20245075225830078)



#Plain
Plain_Error.append(7.511470442125808)
Plain_Time.append(135.76162791252136)


#size
testing.append(388)


#dsi

#SAS 10 2
SAS_Error.append(4.04587065718339)
SAS_Time.append(1.83702731132507 +  0.0488767623901367)


#KMEANS
KMEANS_Error.append(4.247408385087966)
KMEANS_Time.append(3.984320640563965 + 0.17317914962768555)



#Plain
Plain_Error.append(4.096514319996378)
Plain_Time.append(34.384929180145264)


#size
testing.append(348)


#man1

#SAS 6 2 
SAS_Error.append(2.2380142399066107)
SAS_Time.append(35.04469704627991+ 0.24747347831726074 )


#KMEANS
KMEANS_Error.append(2.2407518376984434)
KMEANS_Time.append(20.062305212020874 + 0.18370556831359863 )



#Plain
Plain_Error.append(2.252140391836537)
Plain_Time.append(60.19203209877014)

#size
testing.append(460)


#mint1


#SAS 4 1 
SAS_Error.append(2.4798063300494886)
SAS_Time.append(14.870355367660522 + 0.1273517608642578)


#KMEANS
KMEANS_Error.append(2.447543763620524)
KMEANS_Time.append(1.7101263999938965+ 0.2269296646118164)



#Plain
Plain_Error.append(2.501332325047319)
Plain_Time.append(29.728513717651367)

#size
testing.append(810)



labels=["LIB1","LIB2","SAH1", "TUT5", "TUT6", "UJI1", "UTS1", "DSI1","MAN1", "MINT1"]

plt.style.use('seaborn-whitegrid')

SASNE=[]
SASNT=[]

KMEANSNE=[]
KMEANSNT=[]

PNE=[]
PNT=[]
c=0


for i in range(0,len(Plain_Error)):
	SAS_Time[i] = SAS_Time[i]/testing[i]
	KMEANS_Time[i] = KMEANS_Time[i]/testing[i]
	Plain_Time[i] = Plain_Time[i]/testing[i]

for i in range(0,len(Plain_Error)):
	SASNE.append(SAS_Error[i])
	SASNT.append(SAS_Time[i])

	KMEANSNE.append(KMEANS_Error[i])

	KMEANSNT.append(KMEANS_Time[i])

	PNE.append(Plain_Error[i])
	PNT.append(Plain_Time[i])

	plt.plot(
		[KMEANSNE[i],SASNE[i], PNE[i]],
		[KMEANSNT[i],SASNT[i], PNT[i]],label=labels[c],linewidth=4)
	c+=1





plt.plot(SASNE, SASNT, 'o', color='green',label="SAS",markersize=12);
plt.plot(KMEANSNE, KMEANSNT, 'o', color='brown',label=" $\it{K}$-Means",markersize=12);
plt.plot(PNE, PNT, 'o', color='red',label="Plain $\it{k}$-NN",markersize=12);
plt.xlabel("APE [m]", fontsize=25)
plt.ylabel("Time [s]", fontsize=25)
plt.xticks(fontsize=19)
plt.yticks(fontsize=19)
plt.xlim(0,9.5)
plt.legend(loc='lower left', bbox_to_anchor=(1, 0.2),prop={'size': 15})
plt.show()