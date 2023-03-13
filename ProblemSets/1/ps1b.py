###########################
# 6.0002 Problem Set 1b: Space Change
# Name:
# Collaborators:
# Time:
# Author: charz, cdenise

#================================
# Part B: Golden Eggs
#================================

# Problem 1
def dp_make_weight(egg_weights, target_weight, memo = {})->int:
    """
    Find number of eggs to bring back, using the smallest number of eggs. Assumes there is
    an infinite supply of eggs of each weight, and there is always a egg of value 1.
    
    Parameters:
    egg_weights - tuple of integers, available egg weights sorted from smallest to largest value (1 = d1 < d2 < ... < dk)
    target_weight - int, amount of weight we want to find eggs to fit
    memo - dictionary, OPTIONAL parameter for memoization (you may not need to use this parameter depending on your implementation)
    
    Returns: int, smallest number of eggs needed to make target weight
    """
    # TODO: Your code here
    #take the last value 
    resultTakeVal=0
    resultNoTakeVal =0 
    # if it was already solve - return values 
    if (len(egg_weights),target_weight) in memo:
        return memo[(len(egg_weights),target_weight)]
    
    if len(egg_weights)== 0: 
        raise IndexError # there is infinite amount of eggs with "1" value
    elif len(egg_weights)==1:
        if (egg_weights[0] <= target_weight and (target_weight-egg_weights[0] >= egg_weights[0])):
            resultTakeVal = dp_make_weight(egg_weights,target_weight-egg_weights[0],memo={}) +1
            memo[(len(egg_weights),target_weight)]=resultTakeVal
            return resultTakeVal
        elif (egg_weights[0] <= target_weight and (target_weight-egg_weights[0] < egg_weights[0])):
            #resultTakeVal =  dp_make_weight(egg_weights[0],target_weight-egg_weights,memo={}) +1
            return 1
        else:
            return 0
    elif len(egg_weights)>1:
        if (egg_weights[-1] <= target_weight and (target_weight-egg_weights[-1] >= egg_weights[-1])):
            resultTakeVal = dp_make_weight(egg_weights,target_weight-egg_weights[-1],memo={}) +1
        elif (egg_weights[-1] <= target_weight and (target_weight-egg_weights[-1] < egg_weights[-1])):
            resultTakeVal =  dp_make_weight(egg_weights[:-1],target_weight-egg_weights[-1],memo={}) +1

        resultNoTakeVal = dp_make_weight(egg_weights[:-1],target_weight,memo={})  

        if resultNoTakeVal == 0 and resultTakeVal ==0:
            raise ValueError
        elif resultTakeVal <resultNoTakeVal or resultTakeVal ==0:
            return resultTakeVal
        else:
            return resultNoTakeVal

    
    



# EXAMPLE TESTING CODE, feel free to add more if you'd like
if __name__ == '__main__':
    egg_weights = (1,2,5, 6,7, 25)
    n = 94
    print("Egg weights = (1, 5, 10, 25)")
    print("n = 99")
    print("Expected ouput: 9 (3 * 25 + 2 * 10 + 4 * 1 = 99)")
    print("Actual output:", dp_make_weight(egg_weights, n))
    print()