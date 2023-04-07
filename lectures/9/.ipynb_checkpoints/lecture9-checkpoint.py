import matplotlib.pylab
import pylab

# calculating spring constant 
#
# distances = [0.0865,0.1015,0.1106,0.1279,0.1892,0.2695,0.2888,0.2425,0.3465,0.3225,0.3764,0.42063,0.4562]
# masses = [0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7]
#
# gravityConst = 9.81
# kTab = []
# for d,m in zip(distances,masses):
#     print(d,m)
#     kTab.append(m*gravityConst/d)
#
# k = sum(kTab)/len(list(zip(distances,masses)))
#
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
    pylab.plot(xVals, estYVals, 'r', label="linear fit, k = " + str(round(1/a,5)))
    pylab.legend(loc="best")
    #pylab.show()

fitData("springData.txt")



