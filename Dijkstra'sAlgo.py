# Implementation of Dijkstra's Algorithm in Python
# Importing the sys module
import sys

# Declaring the list of nodes for the graph
nodes = [
    [0, 0, 1, 0, 1, 0, 0],
    [0, 0, 1, 0, 0, 1, 0],
    [1, 1, 0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0, 0, 1],
    [0, 0, 1, 0, 0, 1, 0],
    [0, 1, 0, 0, 1, 0, 1],
    [0, 0, 0, 1, 0, 1, 0]
]

# Declaring the list of edges for the graph
edges = [
    [0, 0, 1, 0, 2, 0, 0],
    [0, 0, 2, 0, 0, 3, 0],
    [1, 2, 0, 1, 3, 0, 0],
    [2, 0, 1, 0, 0, 0, 1],
    [0, 0, 3, 0, 0, 2, 0],
    [0, 3, 0, 0, 2, 0, 1],
    [0, 0, 0, 1, 0, 1, 0]
]

# Defining the function to find which node is to be visited next
def toBeVisited():
    global visitedAndDistance
    v = -10
    for index in range(numberOfNodes):
        if visitedAndDistance[index][0] == 0 and (v < 0 or visitedAndDistance[index][1] <= visitedAndDistance[v][1]):
            v = index
    return v

# Finding the number of nodes in the graph
numberOfNodes = len(nodes[0])

# Initializing the visitedAndDistance list
visitedAndDistance = [[0, 0]]
for i in range(numberOfNodes - 1):
    visitedAndDistance.append([0, sys.maxsize])

# Main loop for Dijkstra's Algorithm
for node in range(numberOfNodes):
    # Finding the next node to be visited
    toVisit = toBeVisited()
    for neighborIndex in range(numberOfNodes):
        # Updating the new distances
        if nodes[toVisit][neighborIndex] == 1 and visitedAndDistance[neighborIndex][0] == 0:
            newDistance = visitedAndDistance[toVisit][1] + edges[toVisit][neighborIndex]
            if visitedAndDistance[neighborIndex][1] > newDistance:
                visitedAndDistance[neighborIndex][1] = newDistance
        visitedAndDistance[toVisit][0] = 1

# Printing the distance
i = 0
for distance in visitedAndDistance:
    print("Distance of", chr(ord('A') + i), "from the source node:", distance[1])
    i = i + 1
