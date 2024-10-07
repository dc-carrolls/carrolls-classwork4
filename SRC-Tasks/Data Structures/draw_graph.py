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
    

