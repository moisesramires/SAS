

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
#BSC
BSC_Error = []
BSC_Time = []



#KMEANS
KMEANS_Error = []
KMEANS_Time = []



#Plain
Plain_Error = []
Plain_Time = []


testing=[]


# N T


#lib1

#BSC 8 -7
BSC_Error.append(2.4382170113098924)
BSC_Time.append(18.32305359840393 + 0.34459400177001953)


#KMEANS
KMEANS_Error.append(2.3356375822289093)
KMEANS_Time.append(1.6486802101135254 + 0.1750338077545166)



#Plain
Plain_Error.append(2.439044375907644)
Plain_Time.append(27.78903102874756)



#size
testing.append(576)


#lib2



#BSC 1 -6
BSC_Error.append(2.4798308653016936)
BSC_Time.append(4.9566380977630615 + 0.07794904708862305)


#KMEANS
KMEANS_Error.append(2.8115578739279865)
KMEANS_Time.append(1.5296635627746582 + 0.1753220558166504 )



#Plain
Plain_Error.append(2.9150480177067597)
Plain_Time.append(26.870366096496582)


#size
testing.append(576)



#sah1

#BSC 1 -7
BSC_Error.append(6.44379930650558)
BSC_Time.append(7.566234827041626 + 0.07243895530700684)


#KMEANS
KMEANS_Error.append(6.042812267703738)
KMEANS_Time.append(22.927672386169434 + 0.08941817283630371)



#Plain
Plain_Error.append(6.250726726257672)
Plain_Time.append(75.26426792144775)

#size
testing.append(156)



#tut5

#BSC 18 0
BSC_Error.append(6.11608126812384)
BSC_Time.append(4.5494270324707 + 0.282880067825317)


#KMEANS
KMEANS_Error.append(6.4543851236371355)
KMEANS_Time.append(1.2746453285217285 + 0.4122936725616455 )



#Plain
Plain_Error.append(6.253951032064151)
Plain_Time.append(14.877002716064453)

#size
testing.append(975)




#tut6

#BSC 7 -5
BSC_Error.append(2.057992409654528)
BSC_Time.append(112.7067346572876+ 3.196178674697876)

#KMEANS
KMEANS_Error.append(2.0925495877101397)
KMEANS_Time.append( 575.4805016517639 + 21.227607011795044)



#Plain
Plain_Error.append(2.0784267649449224)
Plain_Time.append(874.4274911880493)


#size
testing.append(7237)





#uji


#BSC 2 -3
BSC_Error.append(7.887697882780988)
BSC_Time.append(6.607471704483032 + 0.3035736083984375)


#KMEANS
KMEANS_Error.append(8.873737535521615)
KMEANS_Time.append(56.37391257286072 + 0.5578653812408447)



#Plain
Plain_Error.append(8.838846993928243)
Plain_Time.append(680.3997316360474)


#size
testing.append(1111)




#uts1



BSC_Error.append(7.31674836724366)
BSC_Time.append(8.56314492225647+ 0.167251348495483)


#KMEANS
KMEANS_Error.append(7.410185240687027)
KMEANS_Time.append(7.709730625152588+ 0.20245075225830078)



#Plain
Plain_Error.append(7.511470442125808)
Plain_Time.append(135.76162791252136)


#size
testing.append(388)


#dsi

#BSC -20
BSC_Error.append(3.92474625808608)
BSC_Time.append(1.49247932434082 + 0.041573524475098)


#KMEANS
KMEANS_Error.append(4.247408385087966)
KMEANS_Time.append(3.984320640563965 + 0.17317914962768555)



#Plain
Plain_Error.append(4.096514319996378)
Plain_Time.append(34.384929180145264)


#size
testing.append(348)

#man1

#BSC -6 
BSC_Error.append(2.29544634526684)
BSC_Time.append(10.0052270889282 + 0.169227838516235 )


#KMEANS
KMEANS_Error.append(2.2407518376984434)
KMEANS_Time.append(20.062305212020874 + 0.18370556831359863 )



#Plain
Plain_Error.append(2.252140391836537)
Plain_Time.append(60.19203209877014)

#size
testing.append(460)


#mint1


#BSC 4 1 
BSC_Error.append(2.16629505124974)
BSC_Time.append(2.77460980415344 + 0.05893349647522)


#KMEANS
KMEANS_Error.append(2.447543763620524)
KMEANS_Time.append(1.7101263999938965+ 0.2269296646118164)



#Plain
Plain_Error.append(2.501332325047319)
Plain_Time.append(29.728513717651367)

testing.append(810)




labels=["LIB1","LIB2","SAH1", "TUT5", "TUT6", "UJI1", "UTS1", "DSI1","MAN1", "MINT1"]

plt.style.use('seaborn-whitegrid')

BSCNE=[]
BSCNT=[]
SASNE=[]
SASNT=[]


KMEANSNE=[]
KMEANSNT=[]
c=0
for i in range(0,len(Plain_Error)):

	SASNE.append(SAS_Error[i]/Plain_Error[i])
	SASNT.append(SAS_Time[i]/Plain_Time[i])
	BSCNE.append(BSC_Error[i]/Plain_Error[i])
	BSCNT.append(BSC_Time[i]/Plain_Time[i])
	SASNE.append(SAS_Error[i]/Plain_Error[i])
	SASNT.append(SAS_Time[i]/Plain_Time[i])

	KMEANSNE.append(KMEANS_Error[i]/Plain_Error[i])

	KMEANSNT.append(KMEANS_Time[i]/Plain_Time[i])
	plt.plot(
		[BSCNE[i],SASNE[i],KMEANSNE[i]],
		[BSCNT[i],SASNT[i],KMEANSNT[i]],label=labels[c],linewidth=4)
	c+=1








plt.plot(SASNE, SASNT, 'o', color='green',label="SAS",markersize=15);
plt.plot(BSCNE, BSCNT, 'o', color='blue',label="BSC",markersize=15);
plt.plot(KMEANSNE, KMEANSNT, 'o', color='brown',label="$\it{K}$-Means",markersize=15);
plt.plot([1], [1], 'o', color='red',label="Plain $\it{k}$-NN",markersize=15);
plt.xlim(0.8,1.2)
plt.xlabel("Normalized APE [-]", fontsize=25)
plt.ylabel("Normalized Time [-]", fontsize=25)
plt.xticks(fontsize=19)
plt.yticks(fontsize=19)

plt.legend(loc='lower left', bbox_to_anchor=(1, 0.2),prop={'size': 15})
plt.show()