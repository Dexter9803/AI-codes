import heapq

class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    def h(self, n):
        return 1  # You can change this heuristic function as needed.

    def a_star_algorithm(self, start_node, stop_node):
        open_list = [(0, start_node)]  # Priority queue to explore nodes
        heapq.heapify(open_list)  # Heapify the open_list for efficient retrieval
        closed_list = set()  # Set to keep track of explored nodes
        g = {}  # Dictionary to store the cost from start_node to each node
        g[start_node] = 0  # Initialize cost for start_node
        parents = {}  # Dictionary to store parent-child relationships
        parents[start_node] = start_node  # The start_node is its own parent initially
        count = 0

        while open_list:
            _, n = heapq.heappop(open_list)  # Get the node with the lowest cost

            if n == stop_node:
                reconst_path = []
                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]
                reconst_path.append(start_node)
                reconst_path.reverse()
                print('Path found: {}'.format(reconst_path))
                print('Final cost: {}'.format(g[stop_node]))
                return reconst_path

            for (m, weight) in self.get_neighbors(n):
                if m not in closed_list:
                    if m not in g or g[n] + weight < g[m]:
                        g[m] = g[n] + weight
                        count += 1
                        if count == len(self.get_neighbors(n)) + 1:
                            print("Final cost->", g[m])
                        heapq.heappush(open_list, (g[m] + self.h(m), m))
                        parents[m] = n

            closed_list.add(n)  # Mark the node as explored

        print('Path does not exist!')
        return None

node1 = []  # List to store nodes
list_up = []  # List to store neighbor connections and weights
adjacency_list = {}  # Dictionary to store the graph's adjacency list

n1 = int(input("\nEnter the number of nodes in graph->"))
for i in range(n1):
    in1 = input("\nEnter node->")
    node1.append(in1)

for j in range(n1):
    for k in range(j + 1, n1):
        in2 = int(input("Distance between " + str(node1[j]) + " to " + str(node1[k]) + " (PUT -1 FOR NOT CONNECTED)->"))
        if in2 == -1:
            continue
        list_up.append((node1[k], in2))
    if j == (n1 - 1):
        continue
    adjacency_list[node1[j]] = list_up
    list_up = []

print(adjacency_list)  # Display the graph's adjacency list
node_start = input("\nEnter starting node->")
node_end = input("\nEnter ending node->")

if node_start in node1 and node_end in node1:
    graph1 = Graph(adjacency_list)
    graph1.a_star_algorithm(node_start, node_end)
else:
    print("There is some problem in putting the starting or ending node!!")
