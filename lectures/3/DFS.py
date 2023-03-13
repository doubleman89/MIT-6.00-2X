class Node(object):
    def __init__(self,name):
        self.name = name
    def getName(self):
        return self.name
    def __str__(self):
        return self.name


class Edge(object):
    def __init__(self,src : Node,dest : Node):
        self.src = src
        self.dest = dest
    def getSource(self):
        return self.src
    def getDestination(self):
        return self.dest
    def __str__(self):
        return self.src.getName() + '->' + self.dest.getName()   


class Digraph(object):
    def __init__(self):
        self.edges ={}
    
    def addNode(self,node):
        if node in self.edges:
            raise ValueError('Duplicate node')
        else:
            self.edges[node]=[]
    def addEdge(self,edge : Edge):
        src=edge.getSource()
        dest = edge.getDestination()
        if not (src in self.edges and dest in self.edges):
            raise ValueError('Node not in graph')
        self.edges[src].append(dest)
    
    def childrenOf(self,node : Node):
        return self.edges[node]
    # check if diGraph has a specific node 
    def hasNode(self,node):
        return node in self.edges
    
    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result =''
        for src in self.edges:
            for dest in self.edges[src]:
                result = result + src.getName() + '->' \
                    + dest.getName() + '\n'
        return result [:-1] # omit final newline 
    


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self,edge)
        rev = Edge(edge.getDestination(),edge.getSource())
        Digraph.addEdge(self,rev)

        

def buildCityGraph(graphType):
    g = graphType()
    for name in ('Boston', 'Providence', 'New York', 'Chicago',
                 'Denver', 'Phoenix', 'Los Angeles'): #Create 7 nodes
        g.addNode(Node(name))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('Providence')))
    g.addEdge(Edge(g.getNode('Boston'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('Boston')))
    g.addEdge(Edge(g.getNode('Providence'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('New York'), g.getNode('Chicago')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Denver')))
    g.addEdge(Edge(g.getNode('Chicago'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('Phoenix')))
    g.addEdge(Edge(g.getNode('Denver'), g.getNode('New York')))
    g.addEdge(Edge(g.getNode('Los Angeles'), g.getNode('Boston')))
    return g

def BFS(graph: Digraph,src : Node ,dest : Node):
    initial = [src]
    pathsList : list=[initial]

    while len(pathsList)!=0:
        print('newPath:')
        for path in pathsList:
            result =''
            for node in path:
                result = result + node.getName() +'->'
            print (result[:-2])
        # print('Queue:', len(pathsList))
        # for p in pathsList:
        #     print(printPath(p))
        currentPath = pathsList.pop(0)#get and remove oldest path to check
        lastNode = currentPath[-1] # get Last Node from the path




        # print('Current BFS path:', printPath(currentPath))
        # print()

        if lastNode==dest:
            return currentPath
        for nextNode in graph.childrenOf(lastNode):
            if nextNode not  in currentPath:
                newPath= currentPath+[nextNode]
                pathsList.append(newPath)
    return None 

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result             


def shortestPath(graph, start, end):
    """Assumes graph is a Digraph; start and end are nodes
       Returns a shortest path from start to end in graph"""
    return BFS(graph, start, end)

def testSP(source, destination):
    g = buildCityGraph(Digraph)
    sp = shortestPath(g, g.getNode(source), g.getNode(destination))
    if sp != None:
        print('Shortest path from', source, 'to',
              destination, 'is', printPath(sp))
    else:
        print('There is no path from', source, 'to', destination)
        
testSP('Boston', 'Phoenix')
    
        




        
        


    

