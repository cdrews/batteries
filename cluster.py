import csv
import numpy as np
from matplotlib import pyplot
from sklearn import cluster
from sklearn import preprocessing
rows=[]
r = csv.reader(open("results.csv"))
r.next()
for row in r:
    rows.append(row)
rows=np.array(rows)
splt=np.hsplit(rows,(8,9))
data=splt[0]
titles=splt[1]
data=np.array(data)
data_scaled = preprocessing.scale(data.astype(float))
k = 5
kmeans = cluster.KMeans(n_clusters=k)
kmeans.fit(data_scaled)

labels = np.transpose(kmeans.labels_)
print labels
print np.shape(labels)
centroids = kmeans.cluster_centers_
rows = np.hstack((data,titles))
open("clustered.json","w").write(json.dumps(rows))


for i in range(k):
    # select only data observations with cluster label == i
    ds = data[np.where(labels==i)]
    # plot the data observations
    pyplot.plot(ds[:,0],ds[:,1],'o')
    # plot the centroids
    lines = pyplot.plot(centroids[i,0],centroids[i,1],'kx')
    # make the centroid x's bigger
    pyplot.setp(lines,ms=15.0)
    pyplot.setp(lines,mew=2.0)

pyplot.show()

