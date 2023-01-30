import sys
''' I converted the nodes of the graph from alphabetical to numerical order, like this
A -> 0, B -> 1, C -> 2, D -> 3, G -> 4, F -> 5, H -> 6, J -> 7
'''

class Graph: # graph data structure with all the nodes and weights, table, paths visited, paths unvisited, and the source of the graph

    graph = {}
    table = {}
    closestNode = {}
    pathsVisited = []
    pathsUnvisited = []
    source = 0

    def __init__(self):
        self.graph = {}
        self.table = {}
        self.closestNode = {}
        self.pathsVisited = []
        self.pathsUnvisited = []
        self.source = 0

    def declareNodes(self): # declares all the nodes in order of indices
        self.graph[0] = [[1,4],[2,2],[4,7]]
        self.graph[1] = [[0,4],[3,2]]
        self.graph[2] = [[0,2],[4,3],[5,8]]
        self.graph[3] = [[1,2],[4,5],[6,6]]
        self.graph[4] = [[0,7],[2,3],[3,5],[7,4]]
        self.graph[5] = [[7,3],[2,8]]
        self.graph[6] = [[3,6],[7,7]]
        self.graph[7] = [[6,7],[5,3],[4,4]]
        self.closestNode = {0:'',1:'',2:'',3:'',4:'',5:'',6:'',7:''}
        
        print(self.graph)

    # sets the starting node of the graph and loads the table as well as paths unvisited
    def setSource(self, index):
        self.source = index
        for x in range(len(self.graph)):
            if (index == x):
                self.table[x] = 0 #adds to dictionary with value of zero
                self.closestNode[x] = -1
                self.pathsUnvisited.insert(0, x) # adds the node to the front if its the source
            else:
                self.table[x] = sys.maxsize # adds to dictionary with an extremely high value
                self.closestNode[x] = -2
                self.pathsUnvisited.append(x) # adds node normally if it's not the source
        print(self.pathsUnvisited)
        print(self.table)

    def findClosestNode(self, nodeValue, currentNode):
        for x in range(len(currentNode)): # updates the table of nodes based on distances
            # calculates the local distance to a node + distance to get to that node
            distance = currentNode[x][1] + self.table[nodeValue]
            if (distance < self.table[currentNode[x][0]]): 
                self.table[currentNode[x][0]] = distance # updates the distnace to get to that node
                #self.pathsUnvisited.remove(nodeValue)
                #self.orderNode(nodeValue, distance) #calls a method to reorder the nodes
                print("yo")

        distance = sys.maxsize
        if (self.closestNode[nodeValue] == -2): # finds the closest nodes to a set of nodes
                currentDistance = currentNode[x][1]
                if (currentDistance < distance): # if the graph's source is not the current value --> alter to the closest node in dictionary                
                    self.closestNode[nodeValue] = currentNode[x][0]
                    distance = currentDistance 

    def dijkstraPath(self, goal): # main algorithm that finds the shortest path
        
        while (len(self.pathsUnvisited) != 0):
            node = self.pathsUnvisited[0] # finds the node with the smallest distance in the queue
            self.findClosestNode(node, self.graph[node])
            self.pathsVisited.append(node)
            del self.pathsUnvisited[0]
            print(self.pathsUnvisited) # add that node to paths visited
                    
        print(self.table)
        print(self.closestNode)
        #self.returnPath(goal, '')

    # def returnPath(self, lastNode, path): recursion to find the path of the closest nodes
    #     print(self.source)
    #     if (int(lastNode) == int(self.source)):
    #         print("The path starts from " + path)
    #     else:
    #         print('yo')
    #         path = str(lastNode) + " to " + str(self.closestNode[lastNode])
    #         self.returnPath(self.closestNode[lastNode], path)


def main():
    dijkstraGraph = Graph()
    dijkstraGraph.declareNodes()
    dijkstraGraph.setSource(0)
    dijkstraGraph.dijkstraPath(4)

main()
