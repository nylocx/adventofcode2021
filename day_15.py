#%% Initialize
import networkx as nx
import numpy as np

#%% Read input
with open("day_15_input.txt") as f:
    risks = np.genfromtxt(f, dtype=np.uint8, delimiter=1)


#%% Common
def shortest_path(risk_map):
    graph: nx.Graph = nx.grid_2d_graph(*risk_map.shape)
    nx.set_node_attributes(graph, {n: risk_map[n] for n in graph.nodes}, "risk")
    path = nx.shortest_path(
        graph,
        source=(0, 0),
        target=(risk_map.shape[0] - 1, risk_map.shape[1] - 1),
        weight=lambda u, v, d: risk_map[v],
    )

    return sum(graph.nodes[x]["risk"] for x in path[1:])


#%% Part 1
shortest_path(risks)

#%% Part 2
horizontal_risks = np.hstack([risks + i for i in range(5)])
full_risks = np.vstack([horizontal_risks + i for i in range(5)])
full_risks[full_risks > 9] -= 9

shortest_path(full_risks)
