#%% Initialize
import networkx as nx
from collections import Counter

#%% Read input
with open("day_12_input.txt") as f:
    graph = nx.from_edgelist([x.strip().split("-") for x in f])


#%% Part 1
def single_count_caves(cave, visited):
    if cave == "end":
        return 1
    if cave.islower():
        visited.add(cave)
    result = sum([single_count_caves(c, visited) for c in graph[cave] if c not in visited])
    visited.discard(cave)
    return result


single_count_caves("start", set())


#%% Part 2
def double_count_caves(cave, visited, closed=False):
    if cave == "end":
        return 1
    if visited[cave] > 0 and closed:
        return 0
    if cave.islower():
        visited[cave] += 1
        closed |= visited[cave] == 2

    count = sum(double_count_caves(c, visited, closed) for c in graph[cave] if c != "start")
    visited[cave] -= 1

    return count


double_count_caves("start", Counter())
