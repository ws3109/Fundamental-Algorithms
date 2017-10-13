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

def dijkstra(graph, initial):
    INF = float('inf')
    unvisited_nodes = set(graph.nodes)
    dist, path = {}, {}
    for node in unvisited_nodes:
        dist[node] = INF if node != initial else 0
        path[node] = [] if node != initial else [node]
    while len(unvisited_nodes) > 0:
        min_node = None
        for node in unvisited_nodes:
            min_node = node if (min_node is None or dist[node] < dist[min_node]) else min_node
        if dist[min_node] == INF:
            break
        unvisited_nodes.remove(min_node)
        for neighbor in graph.edges[min_node]:
            new_dist =  dist[min_node] + graph.distances[(min_node, neighbor)]
            if new_dist < dist[neighbor]:
                dist[neighbor], path[neighbor] = new_dist, path[min_node] + [neighbor]
    return dist, path

def test():
    n, initial = 100, 0
    g = generateGraph(n)
    dist, path = dijkstra(g, initial)
    for node in dist:
        print("Node %d: " % (node) +'->'.join(map(str, path[node])) + ': '+ str(dist[node]))

test()
