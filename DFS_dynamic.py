def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next_node in graph[start] - visited:
        dfs(graph, next_node, visited)
    return visited

# Function to get user input for the graph
def get_user_input():
    graph = {}
    while True:
        node = input("Enter a node (or type 'done' to finish): ")
        if node.lower() == 'done':
            break
        neighbors = input(f"Enter neighbors for node {node} (comma-separated): ").split(',')
        graph[node] = set(neighbors)
    return graph

# Get user input for the graph
user_graph = get_user_input()

# Get user input for the starting node
user_start_node = input("Enter the starting node: ")

# Call DFS with user input
dfs(user_graph, user_start_node)
