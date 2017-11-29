#	Coder: VShian
#	www.github.com/VShian

from collections import OrderedDict
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

points=list()

f=open('dataset.txt','r')								# get
for line in f:											# the
	x,y=line.split()									# dataset
	points.append((int(x),int(y)))						# from
f.close()												# file

def dis(a,b):											# L2 distance function
	x1,y1=a
	x2,y2=b
	return math.sqrt((x2-x1)**2+(y2-y1)**2)

def iscore(p):											# is 'p' core ? true : false
	count=0												
	reachable_from_p=list()								# set of directly reachable points from point 'p'
	for point in points:
		if dis(p,point) <= radius:
			count+=1
			reachable_from_p.append(point)
	directly_reachable[p]=reachable_from_p				# adding points to global directly reachabkle set
	return count>=minpts

minpts=input('minPts:')
while minpts<=1:
	print "minpts must be atleast 2"
	minpts=input('minpts:')
radius=input('radius:')
while radius<=0:
	print "Radius can't be negative"
	radius=input('radius:')

corepoints=list()
directly_reachable=dict()

for point in points:
	if iscore(point):
		corepoints.append(point)

# print len(corepoints)
# print directly_reachable

corepoints=OrderedDict((x, True) for x in corepoints).keys()
noise=set(points)
clusters=[]
while len(corepoints)!=0:
	cluster=[]
	cluster.append(corepoints[0])
	i=0     
	while i<len(cluster):
		point=cluster[i]
		if point in corepoints:
			cluster+=directly_reachable[point]
			corepoints.remove(point)
			cluster=OrderedDict((x, True) for x in cluster).keys()
		i+=1
	clusters.append(cluster)
	noise=noise-set(cluster)
# print len(clusters)


for cluster in clusters:									# coloring the clusters
	x,y=zip(*cluster)
	plt.scatter(x,y)

if len(noise)>0:											# coloring the noise points
	x,y=zip(*noise)
	plt.scatter(x,y,color='gray')

plt.show()													# display the plotted graph