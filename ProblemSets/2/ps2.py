# 6.0002 Problem Set 5
# Graph optimization
# Name: PD 
# Collaborators:
# Time:

#
# Finding shortest paths through MIT buildings
#
import unittest
from graph import Digraph, Node, WeightedEdge
from copy import deepcopy
#
# Problem 2: Building up the Campus Map
#
# Problem 2a: Designing your graph
#
# What do the graph's nodes represent in this problem? What
# do the graph's edges represent? Where are the distances
# represented?
#
# Answer:
#


# Problem 2b: Implementing load_map
def load_map(map_filename):
    """
    Parses the map file and constructs a directed graph

    Parameters:
        map_filename : name of the map file

    Assumes:
        Each entry in the map file consists of the following four positive
        integers, separated by a blank space:
            From To TotalDistance DistanceOutdoors
        e.g.
            32 76 54 23
        This entry would become an edge from 32 to 76.

    Returns:
        a Digraph representing the map
    """

    # TODO
    campusMap = Digraph()
    with open(map_filename,'r',encoding='utf-8') as file:

        for line in file:
            x= line.split(" ")
            src = Node(x[0])
            dest = Node(x[1])
            distance = x[2]
            distanceOutside = x[3]
            edge = WeightedEdge(src,dest,distance,distanceOutside)
            campusMap.add_node(src)
            campusMap.add_node(dest)
            campusMap.add_edge(edge)
    
    print("Loading map from file...", str(map_filename))
    #print(campusMap)
    return campusMap

# Problem 2c: Testing load_map
# Include the lines used to test load_map below, but comment them out


#
# Problem 3: Finding the Shorest Path using Optimized Search Method
#
# Problem 3a: Objective function
#
# What is the objective function for this problem? What are the constraints?
#objective function - depth first search 
# constraints - shortest total distance traveled, do not exceed max distance outdoors 
# Answer:
#

# Problem 3b: Implement get_best_path
def get_best_path(digraph : Digraph, start : str, end : str, path : list, max_dist_outdoors, best_dist,
                  best_path):
    """
    Finds the shortest path between buildings subject to constraints.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        path: list composed of [[list of strings], int, int]
            Represents the current path of nodes being traversed. Contains
            a list of node names, total distance traveled, and total
            distance outdoors.
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path
        best_dist: int
            The smallest distance between the original start and end node
            for the initial problem that you are trying to solve
        best_path: list of strings
            The shortest path found so far between the original start
            and end node.

    Returns:
        A tuple with the shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k and the distance of that path.

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then return None.
    """
    # TODO
    # get all edge nodes for the start 
    startNode = Node(start)
    endNode = Node(end)
    if not digraph.has_node(startNode) or not digraph.has_node(endNode):
        raise ValueError('Nodes not in a graph')
    
    elif start == end: 
        raise ValueError('start and end are the same nodes')
    
    if not path : 
        path = [[],0,0]
        path[0].append(start)
        path[1] = 0
        path[2] = 0
    
    # if not best_path:
    #     best_path = []
    #     best_dist = 0 
        
    
    possibleDest = digraph.get_edges_for_node(startNode)
    for edges in possibleDest:
        edges : WeightedEdge 
        
        # destination temporary variables
        destNode : Node = edges.get_destination()
        destNodeName =destNode.get_name()
        #create tempPath for every iteration in loop 
        tempPath = deepcopy(path)
        # if next possible destination means that You already made a loop - skip it 
        if destNodeName == start or destNodeName in path[0]:
            continue

        tempPath[0].append(destNodeName)
        tempPath[1] = tempPath[1] + int(edges.get_total_distance())
        tempPath[2] = tempPath[2] + int(edges.get_outdoor_distance())
        
        # if max distance outdoors exceeded - skip it 
        if tempPath[2] > max_dist_outdoors:
            continue
        # check if we reached destination
        elif destNodeName == end:
            if tempPath[1] < best_dist or best_dist == 0:
                best_dist =tempPath[1]
                best_path = tempPath[0]
                return (best_path,best_dist)
        #check if this is final node 
        elif not digraph.get_edges_for_node(destNode) :
            continue
        #else - explore further
        else:
            (best_path,best_dist) = get_best_path(digraph,destNodeName,end,tempPath,max_dist_outdoors,best_dist,best_path)
    
    if not best_path: 
        return (None,0)
    else:
        return (best_path,best_dist)
    

        




# Problem 3c: Implement directed_dfs
def directed_dfs(digraph, start, end, max_total_dist, max_dist_outdoors):
    """
    Finds the shortest path from start to end using a directed depth-first
    search. The total distance traveled on the path must not
    exceed max_total_dist, and the distance spent outdoors on this path must
    not exceed max_dist_outdoors.

    Parameters:
        digraph: Digraph instance
            The graph on which to carry out the search
        start: string
            Building number at which to start
        end: string
            Building number at which to end
        max_total_dist: int
            Maximum total distance on a path
        max_dist_outdoors: int
            Maximum distance spent outdoors on a path

    Returns:
        The shortest-path from start to end, represented by
        a list of building numbers (in strings), [n_1, n_2, ..., n_k],
        where there exists an edge from n_i to n_(i+1) in digraph,
        for all 1 <= i < k

        If there exists no path that satisfies max_total_dist and
        max_dist_outdoors constraints, then raises a ValueError.
    """
    # TODO
    (best_path,best_dist) =get_best_path(digraph, start, end, [], max_dist_outdoors , 0, [])
    if best_path == None or best_dist>max_total_dist:
        raise ValueError ("path does not exist")
    return best_path

# ================================================================
# Begin tests -- you do not need to modify anything below this line
# ================================================================

class Ps2Test(unittest.TestCase):
    LARGE_DIST = 99999

    def setUp(self):
        self.graph = load_map("mit_map.txt")

    def test_load_map_basic(self):
        self.assertTrue(isinstance(self.graph, Digraph))
        self.assertEqual(len(self.graph.nodes), 37)
        all_edges = []
        for _, edges in self.graph.edges.items():
            all_edges += edges  # edges must be dict of node -> list of edges
        all_edges = set(all_edges)
        self.assertEqual(len(all_edges), 129)

    def _print_path_description(self, start, end, total_dist, outdoor_dist):
        constraint = ""
        if outdoor_dist != Ps2Test.LARGE_DIST:
            constraint = "without walking more than {}m outdoors".format(
                outdoor_dist)
        if total_dist != Ps2Test.LARGE_DIST:
            if constraint:
                constraint += ' or {}m total'.format(total_dist)
            else:
                constraint = "without walking more than {}m total".format(
                    total_dist)

        print("------------------------")
        print("Shortest path from Building {} to {} {}".format(
            start, end, constraint))

    def _test_path(self,
                   expectedPath,
                   total_dist=LARGE_DIST,
                   outdoor_dist=LARGE_DIST):
        start, end = expectedPath[0], expectedPath[-1]
        self._print_path_description(start, end, total_dist, outdoor_dist)
        dfsPath = directed_dfs(self.graph, start, end, total_dist, outdoor_dist)
        print("Expected: ", expectedPath)
        print("DFS: ", dfsPath)
        self.assertEqual(expectedPath, dfsPath)

    def _test_impossible_path(self,
                              start,
                              end,
                              total_dist=LARGE_DIST,
                              outdoor_dist=LARGE_DIST):
        self._print_path_description(start, end, total_dist, outdoor_dist)
        with self.assertRaises(ValueError):
            directed_dfs(self.graph, start, end, total_dist, outdoor_dist)

    def test_path_one_step(self):
        self._test_path(expectedPath=['32', '56'])

    def test_path_no_outdoors(self):
        self._test_path(
            expectedPath=['32', '36', '26', '16', '56'], outdoor_dist=0)

    def test_path_multi_step(self):
        self._test_path(expectedPath=['2', '3', '7', '9'])

    def test_path_multi_step_no_outdoors(self):
        self._test_path(
            expectedPath=['2', '4', '10', '13', '9'], outdoor_dist=0)

    def test_path_multi_step2(self):
        self._test_path(expectedPath=['1', '4', '12', '32'])

    def test_path_multi_step_no_outdoors2(self):
        self._test_path(
            expectedPath=['1', '3', '10', '4', '12', '24', '34', '36', '32'],
            outdoor_dist=0)

    def test_impossible_path1(self):
        self._test_impossible_path('8', '50', outdoor_dist=0)

    def test_impossible_path2(self):
        self._test_impossible_path('10', '32', total_dist=100)


if __name__ == "__main__":
    unittest.main()
    # map = load_map("test_load_map.txt")
    # best_Path = directed_dfs(map, "a", "f", 50,11)
    # print(best_Path)