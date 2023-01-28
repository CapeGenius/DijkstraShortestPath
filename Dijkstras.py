# Rohan Bendapudi - 1/24/2023

class Node:
    index = None
    connectedNodes = ()

    def _init_(index):
        self.index = index
class Dijkstra:
    
    pathsVisited = []
    pathsUnvisited = []


    def declareNodes():
        node1 = Node(1)
        node2 = Node(2)
        node3 = Node(3)
        node4 = Node(4)
        node6 = Node(6)
        node7 = Node(7)
        node8 = Node(8)
        node10 = Node(10)
        node1.connectedNodes = ([node3,2],[node2,4],[node7,7])
        node2.connectedNodes = ([node1,4],[node4,2])
        node3.connectedNodes = ([node1,2],[node7,3],[node6,8])
        node4.connectedNodes = ([node2,2],[node7,5],[node8,6])
        node6.connectedNodes = ([node3,8],[node10,3])
        node7.connectedNodes = ([node3,3],[node1,7],[node10,4],[node4,5])
        node8.connectedNodes = ([node10,2],[node4,6])
        node10.connectedNodes = ([node8,2],[node6,3],[node7,4])

        self.pathsUnvisited = [node1, node2, node3, node4, node6, node7, node8, node10]
        self.pathsVisited = []

    
