import networkx as nx
import matplotlib.pyplot as plt

# Parameters
n = 100  # Number of nodes
m = 3     # Number of edges to attach from a new node to existing nodes

# Create a Barabási-Albert graph
G = nx.barabasi_albert_graph(n, m)

# Get the degree of each node
degrees = [G.degree(node) for node in G.nodes()]

# Calculate the degree distribution
degree_distribution = nx.degree_histogram(G)
degree_distribution = [count / float(nx.number_of_nodes(G)) for count in degree_distribution]

# Plot the degree distribution
plt.figure(figsize=(12, 6))
plt.subplot(121)
plt.bar(range(len(degree_distribution)), degree_distribution, width=1.0, color='b')
plt.xlabel('Degree')
plt.ylabel('Frequency')
plt.title('Degree Distribution of Barabási-Albert Graph')

# Plot the graph using a circular layout
plt.subplot(122)
# pos = nx.circular_layout(G)
nx.draw(G, with_labels=False, node_size=30)
plt.title('Barabási-Albert Graph (n={}, m={})'.format(n, m))

plt.tight_layout()
plt.show()
