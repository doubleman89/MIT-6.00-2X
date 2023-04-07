import matplotlib.pylab as pylab
import random
import numpy


class Player(object):
    def __init__(self,name,height,weight) -> None:
        self.name = name
        self.height = height
        self.weight = weight

class Cluster(object):
    def __init__(self,examples,centroids) -> None:
        self.examples = examples
        self.centroids = centroids


def getData(fileName):
    players = []
    with open(fileName,"r") as file:
        for l in file:
            data = l.split(",")
            players.append([data[0],float(data[1]),float(data[2])])
    return players


def preparePlotData(plotData):
    xVals = plotData[1]
    yVals = plotData[2]
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    return xVals,yVals

# def getManhattanDist(val,centroid):
#     dist = []
#     for i in range(len(centroid)):
#         dist.append(abs(centroid[i]-val[i]))
#     return sum(dist)

def getDist(val,centroid,n):
    """Minkowsky method
    for n = 1 - Manhattan distance
    for n = 2 Euclidian distance """
    dist = []
    for i in range(len(centroid)):
        dist.append(abs(centroid[i]-val[i])**n)


    return sum(dist)**1/n

def getClosestCentroid(val,centroids):
    chosenCentroid = None
    chosenDist = 0

    for i in range(len(centroids)):

        valDist = getDist(val,centroids[i],2) 
        if chosenDist == 0 or ((valDist <chosenDist)and chosenDist > 0):
            chosenCentroid = i
            chosenDist = valDist

    return chosenCentroid


def getTrainSamples(vals,centroids):
    

    k = len(centroids)
    clusters = [[]for i in range(k) ]
    for i in range(len(vals)):
        clusters[getClosestCentroid(vals[i],centroids)].append(vals[i])

    means =[]
    for i in range(len(clusters)):
        means.append(list(map(float,numpy.mean(clusters[i],0))))
        print("cluster ",i," = ",clusters[i],"with mean: ",means[i])

    if len(means) != len(centroids):
        raise ValueError("length of previous and next centroids table are different") 
    
    for i in range(len(centroids)):
        if means[i] != centroids[i]:
            getTrainSamples(vals,means)
            break


   
    return clusters

def clusterData(vals,k):
    """byVal - defines if the data will be clustered by:
    1- xVals
    2 - yVals
    3 - xVals,yVals"""
    # picks, median, centroids=[],[],[]
    # for i in range(len(vals)):
    #     median.append(numpy.median(vals[i]))
    centroids =[]
    samples = random.sample(vals,k)
    for i in range(k):   
        centroids.append(samples[i])
    return getTrainSamples(vals,centroids)

    



def generateModel(xVals,yVals):
    model = pylab.polyfit(xVals,yVals,1)
    estYVals = pylab.polyval(model,xVals)
    return estYVals


# generate plot Data
plotData = getData("players.txt")
# generate list of Players
players = [Player(p[0],p[1],p[2]) for p in plotData]
data = [[p.height,p.weight] for p in players]
# generate plot Data
# xVals,yVals = preparePlotData(plotData)
# print(xVals,yVals)

# estYVals = generateModel(xVals,yVals)


# pylab.plot(xVals,yVals,'bo',label = "players data")
# pylab.plot(xVals,estYVals,'r',label = 'fit to data with degree 1')
# pylab.plot(xVals,estYVals,'r',label = 'fit to data with degree 1')
# pylab.legend(loc='best')



clusters =clusterData(data,4)
for i in range(len(clusters)):
    print(clusters[i])





