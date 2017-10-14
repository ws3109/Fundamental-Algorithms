from collections import *
import random

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def add_edge(self, from_node, to_node, distance):
        self.adjList[from_node].append((to_node, distance))
        self.adjList[to_node].append((from_node, distance))

def generateGraph(n, threshold = 0.3, low = 10, high = 100):
    g = Graph()
    for i in range(n):
        for j in range(i+1, n):
            if random.uniform(0, 1) <= threshold:
                g.add_edge(i, j, random.randint(low, high))
    return g

def bellmanFord(graph, initial):
    INF = float('inf')
    dist, path = {}, {}
    for u in graph.adjList:
        dist[u] = INF if u != initial else 0
        path[u] = [] if u != initial else [u]
    for i in range(len(graph.adjList) - 1):
        for u in graph.adjList:
            for v, edge_cost in graph.adjList[u]:
                if dist[v] > dist[u] + edge_cost:
                    dist[v], path[v] = dist[u] + edge_cost, path[u] + [v]
    return dist, path

def test():
    n, initial = 100, 0
    g = generateGraph(n)
    dist, path = bellmanFord(g, initial)
    for u in g.adjList:
        for v, edge_cost in g.adjList[u]:
            assert dist[v] <= dist[u] + edge_cost

test()
