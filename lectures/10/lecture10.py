import matplotlib.pylab as pylab
import random
import numpy
 
def getData(fileName):
    dataFile = open(fileName, 'r')
    distances = []
    masses = []
    dataFile.readline() #discard header
    for line in dataFile:
        d, m = line.split()
        distances.append(float(d))
        masses.append(float(m))
    dataFile.close()
    return (masses, distances)

def rSquared(observed, predicted):
    error = ((predicted - observed)**2).sum()
    meanError = error/len(observed)
    return 1 - (meanError/numpy.var(observed))

def genFits(xVals,yVals,degrees):
    models=[]
    for d in degrees:
        models.append(pylab.polyfit(xVals,yVals,d))
    return models

# generates data
def genNoisyParabolicData(a,b,c,xVals,fName):
    yVals=[]
    for x in xVals:
        theorethicalVal = a*x**2+b*x+c
        yVals.append(theorethicalVal+random.gauss(0,35))
    f=open(fName,'w')
    f.write('x      y\n')
    for i in range(len(yVals)):
        f.write(str(yVals[i])+' '+str(xVals[i])+ '\n')
    f.close()


def testFits(models,degrees,xVals,yVals,fName):
    pylab.plot(xVals,yVals,'ro', label ="Data")
    for i in range(len(models)):
        estYVals = pylab.polyval(models[i],xVals)
        error=rSquared(yVals,estYVals)
        pylab.plot(xVals,estYVals,
                   label = 'Fit of degree '\
                   + str(degrees[i])\
                   + ', R2 = ' + str(round(error, 5)))
    pylab.legend(loc = 'best')
    pylab.title(fName)

# xVals=range(-10,11,1)
# a,b,c = 3,0,0
# genNoisyParabolicData(a,b,c,xVals,'MysterData2.txt')

# degrees=(2,4,8,16)


# random.seed(0) 
# xVals1,yVals1 = getData("MysteryData.txt")
# models1 = genFits(xVals1, yVals1, degrees)
# testFits(models1, degrees, xVals1, yVals1, 'Mystery Data -  model 1') 
# pylab.figure()

# xVals2,yVals2 = getData("MysteryData2.txt")
# testFits(models1, degrees, xVals2, yVals2, 'Mystery Data 2 - model 1' ) 
# pylab.figure()

# models2 = genFits(xVals2, yVals2, degrees)
# testFits(models2, degrees, xVals2, yVals2, 'Mystery Data 2 - model 2' ) 
# pylab.figure()

# testFits(models2, degrees, xVals1, yVals1, 'Mystery Data -  model 2') 
# pylab.figure()



class tempDatum(object):
    def __init__(self,s) -> None:
        info =s.split(',')
        self.high = float(info[1])
        self.year = int(info[2][0:4])

    @property
    def high(self):
        return self._high
    
    @high.setter
    def high(self,value):
        self._high = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self,value):
        self._year = value

def getTempData():
    data=[]
    with open('temperatures.csv') as inFile:
        for l in inFile:
            data.append(tempDatum(l))
    return data

def getTempMean(data):
    """collects all data by year in dict 
    returns temp means for specific year
    return data = tempMean[year]"""
    tempData ={}
    for tempObject in data:
        year =tempObject.year
        high = tempObject.high
        if year in tempData:
            tempData[year].append(high)
        else:
            tempData[year] = [high]
    
    tempMeansData ={}
    for year in tempData:
        tempMeansData[year] = round(sum(tempData[year])/len(tempData[year]),5)
    
    return tempMeansData

def splitData(xVals,yVals):
    toTrain = random.sample(range(len(xVals)),len(xVals)//2)
    trainX, trainY,testX,testY = [],[],[],[]
    for i in range(len(xVals)):
        if i in toTrain:
            trainX.append(xVals[i])
            trainY.append(yVals[i])
        else:
            testX.append(xVals[i])
            testY.append(yVals[i])
    return trainX, trainY,testX,testY 



data =getTempData()
meanData =getTempMean(data)
xVals = pylab.array(list(map(int,meanData.keys())))
yVals =pylab.array(list(map(float,meanData.values())))
# print(xVals)
# print(yVals)

# pylab.plot(xVals,yVals)
# pylab.xlabel('Year')
# pylab.ylabel('Mean Daily High (C)')
# pylab.title('Select U.S. Cities')


numSubsets =100
dimensions = (1,2,3,4)
rSquares = {}
for d in dimensions:
    rSquares[d] =[] 

random.seed(0)

for i in range(numSubsets):   
    trainX, trainY,testX,testY =splitData(xVals,yVals)
    for d in dimensions:
        model = pylab.polyfit(trainX,trainY,d)
        estYVals = pylab.polyval(model,testX)
        rSquares[d].append(rSquared(testY,estYVals))

print('Mean R squares for test data')
for d in dimensions:
    mean = round(sum(rSquares[d])/len(rSquares[d]),4)
    sd = round(numpy.std(rSquares[d]),4)
    print('For dimensionality ',d,'mean = ',mean,'std = ',sd)




