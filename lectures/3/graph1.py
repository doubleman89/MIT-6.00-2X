class Node(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def __str__(self):
        return "dupa"
        


class Edge(object):
    def __init__(self,src,dest):
        self.src=src
        self.dest=dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self) -> str:
        return self.src.getName() + '->'\
            +self.dest.getName()



if __name__ == "__main__":
    Node1 = Node("Alaska")
    Node2 = Node("Daytona")
