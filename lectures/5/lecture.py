import math, random
import matplotlib.pylab as pylab


class Location(object):
    def __init__(self, x:float, y: float):
        " x and y are coordinates - floats"
        self.x = x
        self.y =y 

    def move (self, deltaX : float, deltaY : float):
        return Location(self.x + deltaX,self.y + deltaY)
    

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def distFrom(self,other):
        return math.sqrt((self.x - other.getX())**2 + (self.y - other.getY())**2)
    
    def __str__(self):
        return '<'+str(self.x) + ',' + str(self.y)+ '>'
             
class Drunk (object):
    def __init__(self, name = None):
        self.name = name
    
    def __str__(self):
        if self!= None:
            return self.name
        return 'Anonymous'
    
    def takeStep(self):
        pass
        
class usualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0,1),(0,-1),(1,0), (-1,0)]
        return random.choices(stepChoices)
    
class MasochistDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.1),(0.0,-0.9),(1.0,0.0), (-1.0,0.0)]
        return random.choices(stepChoices)

class Field (object):
    def __init__(self) -> None:
        self.drunks = {}

    def addDrunk(self,drunk,loc):
        if drunk in self.drunks:
            raise ValueError ('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
    
    def getLoc (self,drunk):
        if drunk not in self.drunks:
            raise ValueError("Drunk not in field")
        return self.drunks[drunk]
    
    def moveDrunk (self,drunk):
        if drunk not in self.drunks:
            raise ValueError("drunk not in field")
        [(xDist ,yDist)] = drunk.takeStep()
        #use move method of Location to get new Location 
        self.drunks[drunk] = self.drunks[drunk].move(xDist,yDist)
    
class oddField(Field):
    def __init__(self,numHoles =1000,xRange=100,yRange=100):
        Field.__init__(self)
        self.wormholes = {}
        for w in range(numHoles):
            x=random.randint(-xRange,xRange)
            y=random.randint(-yRange,yRange)
            newX=random.randint(-xRange,xRange)
            newY=random.randint(-yRange,yRange)
            newLoc = Location(newX,newY)
            self.wormholes[(x,y)] = newLoc
    
    def moveDrunk(self, drunk):
        super().moveDrunk(drunk)
        x = self.drunks[drunk].getX()
        y = self.drunks[drunk].getY()
        if (x,y) in self.wormholes:
            self.drunks[drunk] = self.wormholes[(x,y)]
    
class StyleIterator(object):
    def __init__(self,styles):
        self.index = 0
        self.styles=styles
    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles)-1:
            self.index = 0
        else:
            self.index+=1
        return result






   




