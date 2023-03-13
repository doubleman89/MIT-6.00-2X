from  lecture import *

def drunkTest(walkLengths,numTrials,dClass):
    """assumes walkLenghts = sequnce of ints >= 0
        numTrials an int >0 
        dclass = subclass of Drunk"""
    
    def walk(f : Field,d,numSteps):
        """Assumes: f a Field , d a Drunk in f adn numSteps an int >=0
        Moves d numSteps time ; returns the distanfce between the final location and the location at the start 
        of the walk """
        start = f.getLoc(d)
        for s in range (numSteps):
            f.moveDrunk(d)
        return start.distFrom(f.getLoc(d))

    def simWalks(numSteps,numTrials,dClass):
        Homer = dClass()
        origin = Location(0,0)
        distances = []

        for t in range (numTrials):
            f=Field()
            f.addDrunk(Homer,origin)
            distances.append(round(walk(f,Homer,numSteps),1))

        return distances
    # x vals will be number of steps 
    xVals =[]
    # y vals will be distance mean
    yVals = []
    for numSteps in walkLengths:
        xVals.append(numSteps)
        distances = simWalks(numSteps,numTrials,dClass)
        print(dClass.__name__,'random walk of ', numSteps,'steps')
        mean = round(sum(distances)/len(distances),4)
        yVals.append(mean)
        print('Mean = ', mean)
        print(' Max = ', max(distances))
        print(' Min = ', min(distances))
    return xVals,yVals


def locationTest(numSteps,numTrials,dClass):

    Homer = dClass()
    origin = Location(0,0)
    # x coordinates of a Drunk
    xVals =[]
    # y coordinates of a Drunk
    yVals = []
    for t in range (numTrials):
        f=oddField()
        f.addDrunk(Homer,origin)
        for s in range (numSteps):
            f.moveDrunk(Homer)
            location = f.getLoc(Homer)
            xVals.append(location.getX())
            yVals.append(location.getY())

    return xVals,yVals

def simWalkDistance(dClassList,walkLengths,numTrials):
    xValList=[]
    yValList=[]
    for dClass in dClassList:
        xVals,yVals = drunkTest(walkLengths,numTrials,dClass)
        pylab.plot(xVals,yVals,label = dClass.__name__)

    pylab.legend()

def simWalkLocation(dClassList,walkLengths,numTrials):
    xValList=[]
    yValList=[]
    #styleChoice = StyleIterator(('.','o','v','^'))
    styleChoice = StyleIterator(('k+', 'r^', 'mo'))
    for dClass in dClassList:
        
        for numSteps in walkLengths:
            curStyle = styleChoice.nextStyle()
            xVals,yVals = locationTest(numSteps,numTrials,dClass)
            pylab.plot(xVals,yVals,curStyle,label = f"numSteps: {numSteps} for {dClass.__name__}")
        pylab.title('Location at End of Walks ('
                + str(numSteps) + ' steps)')
    pylab.ylim(-1000, 1000)
    pylab.xlim(-1000, 1000)
    pylab.xlabel('Steps East/West of Origin')
    pylab.ylabel('Steps North/South of Origin')
    pylab.legend(loc = 'lower center')
    pylab.legend()
    pylab.show()


if __name__ == "__main__":
    # drunkTest((10,100,1000,10000),100,usualDrunk)
    # # drunkTest((0,1,2),100,usualDrunk)
    
    #simWalkDistance((usualDrunk,MasochistDrunk),(10,100,1000,10000,100000),100)
    simWalkLocation((usualDrunk,MasochistDrunk),(10000,),100)