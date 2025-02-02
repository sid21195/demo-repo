import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

"""Example of a simple neural network with 4 inputs and 1 output."""
inputs: list[int] = [1.0, 2.0, 2.5, 3.0]
weights: list[int] = [2.0, 4.0, -5.0, 6.0]
BIAS = 1.0

output = inputs[0]*weights[0] + inputs[1]*weights[1] + \
    inputs[2]*weights[2] + inputs[3]*weights[3] + BIAS
print(output)

# Output: 16.5

# Using numpy for a more scalable solution
# Example of a simple neural network with 3 neurons and 4 inputs

inputs = np.array([1.0, 2.0, 2.5, 3.0])
weights = np.array([[2.0, 4.0, -5.0, 6.0],
                    [1.0, -2.0, 3.0, -1.0],
                    [0.5, -1.5, 2.0, 1.0]])
BIAS = np.array([1.0, 2.0, 0.5])

output = np.dot(weights, inputs) + BIAS
print(output)

# Output: [16.5  4.5  6.5]

"""Visualizing the Neural Network Structure"""


# Define input values
inputs = np.array([1.0, 2.0, 2.5, 3.0])
weights = np.array([[2.0, 4.0, -5.0, 6.0],
                    [1.0, -2.0, 3.0, -1.0],
                    [0.5, -1.5, 2.0, 1.0]])
biases = np.array([1.0, 2.0, 0.5])

# Compute outputs
outputs = np.dot(weights, inputs) + biases

# Create Graph
G = nx.DiGraph()

# Add nodes
input_nodes = [f"I{i+1}" for i in range(len(inputs))]
hidden_nodes = [f"H{i+1}" for i in range(len(outputs))]

for node in input_nodes + hidden_nodes:
    G.add_node(node)

# Add edges with weights
for i in range(len(weights)):
    for j in range(len(inputs)):
        G.add_edge(input_nodes[j], hidden_nodes[i], weight=weights[i, j])

# Layout
pos = {}
for i, node in enumerate(input_nodes):
    pos[node] = (0, -i)
for i, node in enumerate(hidden_nodes):
    pos[node] = (1, -i)

# Draw graph
plt.figure(figsize=(8, 5))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", edge_color="gray", font_size=10, font_weight="bold")

# Draw edge labels (weights)
edge_labels = {(input_nodes[j], hidden_nodes[i]): f"{weights[i, j]:.1f}" for i in range(len(weights)) for j in range(len(inputs))}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=9)

# Draw output labels
for i, node in enumerate(hidden_nodes):
    plt.text(pos[node][0] + 0.1, pos[node][1], f"{outputs[i]:.1f}", fontsize=12, color="red", fontweight="bold")

plt.title("Simple Neural Network Visualization")
plt.show()
