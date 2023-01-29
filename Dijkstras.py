# Rohan Bendapudi - 1/24/2023
# I converted 
class Graph: # graph data structure with all the nodes and weights, table, paths visited, paths unvisited, and the source of the graph

    graph = {}
    table = {}
    pathsVisited = []
    pathsUnvisited = []
    source = int

    def __init__(self):
        self.graph = {}
        self.table = {}
        self.pathsVisited = []
        self.pathsUnvisited = []
        self.source = int

    def declareNodes(self): # declares all the nodes in order of indices
        self.graph[0] = [[1,4],[2,2],[4,7]]
        self.graph[1] = [[0,4],[3,2]]
        self.graph[2] = [[0,2],[4,3],[5,8]]
        self.graph[3] = [[1,2],[4,5],[6,6]]
        self.graph[4] = [[0,7],[2,3],[3,5],[7,4]]
        self.graph[5] = [[7,3],[2,8]]
        self.graph[6] = [[3,6],[7,7]]
        self.graph[7] = [[6,7],[5,3],[4,4]]
        
        print(self.graph)

    # sets the starting node of the graph and loads the table as well as paths unvisited
    def setSource(self, index):
        self.source = index
        for x in range(len(self.graph)):
            if (index == x):
                self.table[x] = 0 #adds to dictionary with value of zero
                self.pathsUnvisited.insert(0, x) # adds the node to the front if its the source
            else:
                self.table[x] = 100000000000 # adds to dictionary with an extremely high value
                self.pathsUnvisited.append(x) # adds node normally if it's not the source
        print(self.pathsUnvisited)
        print(self.table)
    
    def orderNode(self, nodeValue, dist): # mimics "priority" in queue to insert in proper location based on length
        for x in range(len(self.pathsUnvisited)):
            if (self.table[self.pathsUnvisited[x]] > dist):
                self.pathsUnvisited.insert(x, nodeValue) # inserts the value of the node in its proper location

    def nodeWorks(self, nodeValue, currentNode):
        for x in range(len(currentNode)): # updates the table of nodes based on distances
            # calculates the local distance to a node + distance to get to that node
            distance = currentNode[x][1] + self.table[nodeValue]
            if (distance < self.table[currentNode[x][0]]): 
                self.table[currentNode[x][0]] = distance # updates the distnace to get to that node
                self.pathsUnvisited.remove(nodeValue)
                self.orderNode(nodeValue, distance) #calls a method to reorder the nodes

    def dijkstraPath(self, goal): # main algorithm that finds the shortest path
        
        while (len(self.pathsUnvisited) != 0):
            node = self.pathsUnvisited[0]
            self.nodeWorks(node, self.graph[node])
            self.pathsVisited.append(node)
            del self.pathsUnvisited[0]
                    
        print(self.table)

def main():
    dijkstraGraph = Graph()
    dijkstraGraph.declareNodes()
    dijkstraGraph.setSource(0)
    dijkstraGraph.dijkstraPath(2)

main()
