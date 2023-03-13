###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    # open file
    cows_dict = {}
    with open(filename,'r',encoding='utf-8') as file:

        for line in file:
            x= line.split(",")
            #cow = Cow(x[0],int(x[1].strip("\n")))
            #cows_dict[Cow.getName(cow)] = Cow.getWeight(cow)
            cows_dict[x[0]] =int(x[1].strip("\n"))
    return cows_dict
# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #load data
    """Assumes items a list, maxCost >= 0,
         keyFunction maps elements of items to numbers"""
    #sort data by item value
    itemsCopy = sorted(cows.items(),key=lambda item:item[1],reverse=True)
    # create empty list
    result =[]
    
    while len(itemsCopy) > 0: 
        #create empty list for every shipment
        newList =[]
        #declare initial limit for every shipment
        itemsLimit= limit
        #declare initial removed items for every shipment
        rmItemsCounter = 0    
        print(itemsCopy) 
        for i in range(len(itemsCopy)):
            #include removed items during loop 
            k = i-rmItemsCounter
            #get a tuple
            item=itemsCopy[k]
            #check if value fits limit - if yes - add it to the shipment and remove from sorted list 
            if item[1] <= itemsLimit:
                newList.append(item[0])
                itemsLimit -= item[1]
                rmItemsCounter+=1
                itemsCopy.remove(itemsCopy[k])
            #check if limit was exeeded, if yes - generate list for shipment
            if itemsLimit >= limit:
                result.append(newList)
                break
        #if everthing was checked - generate list for shipment
        result.append(newList)
    return result


# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    pass
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass

cows = load_cows("ps1_cow_data.txt")
print(greedy_cow_transport(cows))