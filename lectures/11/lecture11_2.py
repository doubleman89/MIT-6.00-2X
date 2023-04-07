import matplotlib.pylab as pylab
import random
import numpy


class Player(object):
    def __init__(self,name,features) -> None:
        self.name = name
        self.features = features
        
    def distance(self,other):
        return getDist(self.features,other,2)
    
    def __str__(self) -> str:
        result = self.name + " with features : " + str(self.features)
        return result

class Cluster(object):
    def __init__(self,examples, centroids) -> None:
        self.examples = examples
        self.centroids = centroids
    
    def update(self,examples):
        oldCentroids = self.centroids
        self.examples = examples
        self.centroids = self.calcCentroids()
        return self.centroidsChanged(oldCentroids)

    def calcCentroids(self):
        allFeatures =[]
        for example in self.examples:
            allFeatures.append(example.features)
        return list(map(float,numpy.mean(allFeatures,0)))
    
    def centroidsChanged(self,oldCentroids):
        for i in range(len(self.centroids)):
            if oldCentroids[i] != self.centroids[i]:
                return False
        return True
    
    def members(self):
        for e in self.examples:
            yield e
    
    def variability(self):
        totDist = 0
        for e in self.examples:
            totDist += (e.distance(self.centroids))**2
        return totDist

    def __str__(self) -> str:
        text =""
        for e in self.examples:
            text += str(e) +","
        return "cluster with centroids " + str(self.centroids) +" contains following players : " + text[:-1]


def scaleAttrs(vals):
    vals = pylab.array(vals)
    mean = sum(vals)/len(vals)
    sd = numpy.std(vals)
    vals = vals - mean
    return vals/sd

def getData(fileName, toScale = False):
    players = []
    heights =[]
    weights =[]
    with open(fileName,"r") as file:
        for l in file:
            data = l.split(",")
            players.append([data[0],float(data[1]),float(data[2])])
            if toScale:
                heights.append(float(data[1]))
                weights.append(float(data[2]))

    if toScale:
        heights = scaleAttrs(heights)
        weights = scaleAttrs(weights)
        for i in range(len(players)): 
            players[i][1] = heights[i]
            players[i][2] = weights[i]
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

def getDist(example,other,n):
    """Minkowsky method
    for n = 1 - Manhattan distance
    for n = 2 Euclidian distance """
    dist = []
    for i in range(len(other)):
        dist.append(abs(other[i]-example[i])**n)


    return sum(dist)**1/n

def getClosestCentroid(example : Player,clusters):
    chosenCentroid = None
    chosenDist = 0

    for i in range(len(clusters)):
        valDist = example.distance(clusters[i].centroids)
        if chosenDist == 0 or ((valDist <chosenDist)and chosenDist > 0):
            chosenCentroid = i
            chosenDist = valDist

    return chosenCentroid


def getTrainSamples(examples,centroids):
    

    k = len(centroids)
    clusters = [Cluster(examples,centroids[i].features) for i in range(k) ]
    
    centroidsChanged = True
    while centroidsChanged:
        newExamples =[[]for i in range(k)]
        for i in range(len(examples)):
            newExamples[getClosestCentroid(examples[i],clusters)].append(examples[i])
        
        centroidsChanged = False
        for i in range(len(clusters)):
            if clusters[i].update(newExamples[i]) == True:
                centroidsChanged = True
   
    return clusters

def clusterData(examples,k):
    """byVal - defines if the data will be clustered by:
    1- xVals
    2 - yVals
    3 - xVals,yVals"""

    centroids =[]
    samples = random.sample(examples,k)
    for i in range(k):   
        centroids.append(samples[i])
    return getTrainSamples(examples,centroids)


def dissimilarity(clusters):
    """Assumes clusters a list of clusters
       Returns a measure of the total dissimilarity of the
       clusters in the list"""
    totDist = 0
    for c in clusters:
        totDist += c.variability()
    return totDist




def generateModel(xVals,yVals):
    model = pylab.polyfit(xVals,yVals,1)
    estYVals = pylab.polyval(model,xVals)
    return estYVals


# generate plot Data
plotData = getData("players.txt",True)
# generate list of Players
players = [Player(p[0],[p[1],p[2]]) for p in plotData]
# generate plot Data
# xVals,yVals = preparePlotData(plotData)
# print(xVals,yVals)

# estYVals = generateModel(xVals,yVals)


# pylab.plot(xVals,yVals,'bo',label = "players data")
# pylab.plot(xVals,estYVals,'r',label = 'fit to data with degree 1')
# pylab.plot(xVals,estYVals,'r',label = 'fit to data with degree 1')
# pylab.legend(loc='best')



clusters =clusterData(players,2)
for i in range(len(clusters)):
    print(clusters[i])
    print("variability :" ,str(clusters[i].variability()))

print("clusters dissimilarity :" ,dissimilarity(clusters))





