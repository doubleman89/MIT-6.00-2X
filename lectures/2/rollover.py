def rollover(ps1,ps2,ps3,ps4,ps5,F):
    def score(paramF,valuesSum,F):
        return (60-paramF)*F+valuesSum


    def rolloverHelper(values,paramF,valuesSum): 
        if len(values)==2:
            if paramF ==10:
                return [10],score(paramF+10,valuesSum+values[0]*10,values[1])
            
            resultWith10 = score(paramF+10,valuesSum+values[0]*10,values[1])
            resultWith0 = score(paramF,valuesSum,values[1])
            #check better result
            if resultWith10> resultWith0:
                return [10],resultWith10
            else:
                return [0],resultWith0
            
        
            
        #check route with 10     
        paramList10, resultWith10 = rolloverHelper(values[1:],paramF+10,valuesSum+values[0]*10)
        
        # do not check result with 0 if the constraints will be not fulfilled
        if len(values)==3 and paramF == 0:
            return [10] + paramList10 ,resultWith10
        #check result with 0 
        paramList0, resultWith0 =rolloverHelper(values[1:],paramF,valuesSum)
        
        #check better result
        if resultWith10> resultWith0:
            return [10]+paramList10,resultWith10
        else:
            return [0]+paramList0,resultWith0

    
    values=[ps1,ps2,ps3,ps4,ps5,F]
    paramList,result = rolloverHelper(values,0,0)

    return paramList,result


print(rollover(2,2,2,2,2,10))
print(rollover(10,2,2,2,2,10))
print(rollover(10,2,3,4,5,10))

