import math

def SearchedTreeHelper (count):
    if count == 1:
        return [[1],[0]]
    elif count>1 :

        for i in range(2,count+1):
            result=[]
            for options in SearchedTreeHelper(i-1):
                item1 =options.copy()
                item1.extend([0])
                result.append(item1)
                item2 = options.copy()
                item2.extend([1])
                result.append(item2)
        return result


def SearchedTree(mealsDict,limit):
    possibleOptions = SearchedTreeHelper(len(mealsDict))

    bestOptionDict ={}
    tempDict = {}
    maxValue = 0 
    for elements in possibleOptions:
        i = 0 
        value =0
        for keys in mealsDict:
            
            if keys in mealsDict:
                tempDict.update({keys:int(mealsDict.get(keys))*int(elements[i])})
            else:
                tempDict[keys] = int(mealsDict.get(keys))*int(elements[i])
            i+=1
            value = value + int(tempDict[keys])
# check if the new entry is the best solutin                
        if (maxValue ==0 or value >maxValue) and value <= limit : 
            bestOptionDict = tempDict.copy()
            maxValue = value
    
    return bestOptionDict

mealsDict = {"kanapka":100, "burger":340, "hotdog": 240, "cola" : 190}


print(SearchedTree(mealsDict,440))
print(SearchedTree(mealsDict,580))


print(SearchedTree(mealsDict,579))

print(SearchedTree(mealsDict,770))
print(SearchedTree(mealsDict,769))