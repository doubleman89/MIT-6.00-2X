# From codereview.stackexchange.com                    
class Cow(object):
    instances=[]
    def __init__(self,name,weight):
        self.name=name
        self.weight = weight
        self.__class__.instances.append(self)
    
    def getWeight(self):
        return self.weight 
    def getName(self):
        return self.name


def partitions(set_):
    if not set_:
        yield []
        return
    for i in range(2**len(set_)//2):
        parts = [set(), set()]
        for item in set_:
            parts[i&1].add(item)
            i >>= 1
        for b in partitions(parts[1]):
            yield [parts[0]]+b

def load_cows(cowsList):
    cows_dict={}
    for cow in cowsList:
        cows_dict[cow.getName()] = cow.getWeight()
    return cows_dict






def get_partitions(set_):
    for partition in partitions(set_):
        #print("comment1 :", partition)
        yield [list(elt) for elt in partition]


# cow1 = Cow("amy",10)     
# cow2 = Cow("pammy",20)
# cow3 = Cow("maggie",30)
# cowsList = ([cow1,cow2,cow3])
# cows_dict = load_cows(cowsList)
# for partition in get_partitions(cows_dict):
#     for cows in partition:
#         print(cows)
#         for cow in cows:
#             print(type(cow))
#             print(cows_dict[cow])