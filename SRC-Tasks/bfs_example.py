from collections import deque

def bfs_shortest_path(graph, start):
    # Dictionary to store the distance and path from the start node to each node
    distance = {node: float('inf') for node in graph}
    path = {node: [] for node in graph}
    
    # Initialize the distance to the start node as 0
    distance[start] = 0
    
    # Queue for BFS traversal
    queue = deque([start])
    
    while queue:
        current_node = queue.popleft()
        
        # Explore neighbors of the current node
        for neighbor in graph[current_node]:
            if distance[neighbor] == float('inf'):
                # If the neighbor has not been visited, update its distance and path, and enqueue
                distance[neighbor] = distance[current_node] + 1
                path[neighbor] = path[current_node] + [current_node]
                queue.append(neighbor)
    
    return path

# Example graph represented as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E', 'F'],
    'D': ['B', 'G'],
    'E': ['C', 'H'],
    'F': ['C', 'I'],
    'G': ['D', 'J', 'K'],
    'H': ['E', 'K', 'L'],
    'I': ['F', 'L', 'J'],
    'J': ['G', 'I'],
    'K': ['G', 'H'],
    'L': ['H', 'I']
}

# Starting node for BFS
start_node = 'F'

paths = bfs_shortest_path(graph, start_node)

# Print the shortest paths from the start node to every other node
for node, path in paths.items():
    print(f"Shortest path from {start_node} to {node}: {path + [node]}")


# importing networkx 
import networkx as nx
# importing matplotlib.pyplot
import matplotlib.pyplot as plt

g = nx.Graph()

for node in graph:
    for target in graph[node]:
        g.add_edge(node, target)

while True:
    nx.draw(g, with_labels = True)
    #plt.savefig("graph"+str(i)+".png")
    plt.show()
    plt.clf()
    if input('Try again [y/n]').lower() != 'y':
        break
    

