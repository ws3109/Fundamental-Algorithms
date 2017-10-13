import collections
import random

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = collections.defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.distances[(from_node, to_node)] = distance

    def __str__(self):
        return '\n'.join([' '.join([str(a[0]), str(a[1]),str(self.distances[a])])for a in self.distances])

def generateGraph(n, threshold = 0.3, low = 10, high = 1000):
    g = Graph()
    for i in range(n):
        g.add_node(i)
    for i in range(n):
        for j in range(n):
            if random.uniform(0, 1) <= threshold:
                g.add_edge(i, j, random.randint(low, high))
    return g

def bellmanFord(graph, initial):
    INF = float('inf')
    dist = {}
    for node in graph.nodes:
        dist[node] = INF if node != initial else 0

    # n - 1 times of upates
    for i in range(len(graph.nodes) - 1):
        for node in graph.nodes:
            for neighbor in graph.edges[node]:
                dist[neighbor] = min(dist[neighbor], dist[node] + graph.distances[(node, neighbor)])

    # Check for negative-weight cycles
    for u in graph.nodes:
        for v in graph.edges[u]:
            assert dist[v] <= dist[u] + graph.distances[(u,v)]
    return dist

def test():
    n, initial = 100, 0
    g = generateGraph(n)
    dist = bellmanFord(g, initial)
    for node in dist:
        print("Node %d: " % (node) + ': '+ str(dist[node]))

test()
