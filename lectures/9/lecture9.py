import matplotlib.pylab as pylab
import numpy
import random

#calculating spring constant 

# distances = [0.0865,0.1015,0.1106,0.1279,0.1892,0.2695,0.2888,0.2425,0.3465,0.3225,0.3764,0.42063,0.4562]
# masses = [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7]

# gravityConst = 9.81
# kTab = []
# for d,m in zip(distances,masses):
#     print(d,m)
#     kTab.append(m*gravityConst/d)

# k = sum(kTab)/len(list(zip(distances,masses)))

# print(kTab)
# print(k)

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

def labelPlot():
    pylab.title('Measured Displacement of Spring')
    pylab.xlabel('|Force| (Newtons)')
    pylab.ylabel('Distance (meters)')


def preparePlotData(fileName):
    xVals,yVals = getData(fileName)
    xVals = pylab.array(xVals)
    yVals = pylab.array(yVals)
    xVals =xVals*9.81 # acc. due to gravity
    return xVals,yVals



def fitData(fileName):
    xVals,yVals = preparePlotData(fileName)
    pylab.plot(xVals, yVals,'bo', label="Measured displacements")
    labelPlot()
    a,b = pylab.polyfit(xVals,yVals,1)
    estYVals = a*pylab.array(xVals)+b
    print('a= ', a ,'b= ',b)
    checkError(yVals,estYVals)
    pylab.plot(xVals, estYVals, 'r', label="linear fit, k = " + str(round(1/a,5)))
    pylab.legend(loc="best")
    #pylab.show()

def fitData1(fileName,polyNum):
    xVals,yVals = preparePlotData(fileName)
    pylab.plot(xVals, yVals,'bo', label="Measured displacements")
    labelPlot()
    model = pylab.polyfit(xVals,yVals,polyNum)
    estYVals = pylab.polyval(model,xVals)
    checkError(yVals,estYVals)
    pylab.plot(xVals, estYVals, 'r', label="linear fit, k = " + str(round(1/model[0])))
    pylab.legend(loc="best")
    #pylab.show()

def checkError(yVals,estYVals):

    minVal = min(abs(yVals-estYVals))
    #maxVal = max(abs(yVals-estYVals))
    maxVal = sum(abs(yVals-estYVals))/len(yVals)
    print("Min val is :", minVal, "Average val is : ", maxVal)
    return minVal,maxVal
    


# written by PD, to check if this will be valid with the science theory :) 
def findBestFit(fileName,polyNumMin,polyNumMax): 
    xVals,yVals = preparePlotData(fileName)
    pylab.plot(xVals, yVals,'bo', label="plot data")

    minVal,maxVal,bestPolyNum = None, None, None
    for polyNum in range(polyNumMin,polyNumMax+1):
        model = pylab.polyfit(xVals,yVals,polyNum)
        estYVals = pylab.polyval(model,xVals)
        minValCheck, maxValCheck = checkError(yVals,estYVals)
        if maxVal == None or maxValCheck < maxVal: 
            bestModel = model
            bestEstYVals = estYVals
            minVal,maxVal, bestPolyNum = minValCheck,maxValCheck, polyNum
            
    pylab.plot(xVals, bestEstYVals, 'r', label="best fit with polyNumm = " +str(bestPolyNum) + " and average error = " + str(round(maxVal,5)))
    pylab.legend(loc="best")   



def rSquared(observed,predicted):
    error = ((observed-predicted)**2).sum()
    meanError = error/len(observed)
    return 1 - (meanError/numpy.var(observed)) # (error/len)/(varianceNom/len) = error/VarianceNom


def findBestFit2(fileName,degrees):
    xVals,yVals = preparePlotData(fileName)
    pylab.plot(xVals, yVals,'bo', label="plot data")

    bestError,bestPolyNum = None, None
    for polyNum in degrees:
        model = pylab.polyfit(xVals,yVals,polyNum)
        estYVals = pylab.polyval(model,xVals)
        error =rSquared(yVals,estYVals)
        pylab.plot(xVals, estYVals, 'r', label="fit with fit of degree = " +str(polyNum) + " and R2 = " + str(round(error,5)))        
        if bestError == None or (error > bestError and error <=1): 
            bestModel = model
            bestEstYVals = estYVals
            bestError, bestPolyNum = error, polyNum
    pylab.legend(loc="best")   
    pylab.title('Finding best fit')




#fitData("springData.txt")
#fitData1("springData.txt",1)
#fitData1("mysteryData.txt",2)
#findBestFit("mysteryData.txt",1,4)
#findBestFit2("springData.txt",1,4)
#findBestFit("springData.txt",1,4)
findBestFit2("mysteryData.txt",(2,4,8,16))
#findBestFit("mysteryData.txt",1,4)




