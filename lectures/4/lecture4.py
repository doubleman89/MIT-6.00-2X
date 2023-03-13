import random,math
def rollDie():
    return random.randint(1,6)

def runSim(goal,numTrials,txt):
    total = 0 
    for i in range(numTrials):
        result =''
        for j in range(len(goal)):
            result +=str(rollDie())
        if result == goal:
            total+=1
    print ('Actual probability of', txt,"=",
            round(1/(6**len(goal)),8))
    estProbability = round (total/numTrials,8)
    print('Estimated probability of', txt,'=',round(estProbability,8))
#runSim("11111",1111111,"11111")


def sameDate(numPeople, numSame):
    #possibleDates = range(366)
    possibleDates = 4*list(range(0,57)) + [58]+ 4*list(range(59,366)) + 4*list(range(180,270))
    birthdays = [0]*366
    for p in range (numPeople):
        birthDate = random.choice(possibleDates)
        birthdays[birthDate] +=1
    return max(birthdays) >= numSame

def birthdayProb(numpeople,numSame,numTrials):
    numHits = 0
    for t in range(numTrials):
        if sameDate(numpeople,numSame):
            numHits+=1
    return numHits/numTrials

for i in range (2,4):
    for numPeople in[10,20,40,80,100 ]:
        print('For',numPeople, 'est. prob of', i, 'people with shared birthday is', birthdayProb(numPeople,2,10000))
        numerator = math.factorial(366)
        denom = (366**numPeople)*math.factorial(366-numPeople)
        print ('Actual prob for N = ', numPeople, 1- numerator/denom)
          

