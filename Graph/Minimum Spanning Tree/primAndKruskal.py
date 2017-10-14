from collections import *
import random

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def add_edge(self, from_node, to_node, distance):
        self.adjList[from_node].append((to_node, distance))
        self.adjList[to_node].append((from_node, distance))

    def __str__(self):
        return '\n'.join([str(x) + str(self.adjList[x]) for x in self.adjList])

def generateGraph(n, threshold = 1, low = 1, high = 10):
    g = Graph()
    for i in range(n):
        for j in range(i+1, n):
            if random.uniform(0, 1) <= threshold:
                g.add_edge(i, j, random.randint(low, high))
    return g

def prim(graph):
    cost, INF = 0, float('inf')
    initial = random.choice(list(graph.adjList.keys()))
    span_tree, parent, dist, unvisited_nodes = [], {initial: initial}, {}, set(graph.adjList.keys())
    for u in graph.adjList:
        dist[u] = INF if u != initial else 0
    while len(unvisited_nodes) > 0:
        u = min(unvisited_nodes, key = lambda x: dist[x])
        unvisited_nodes.remove(u)
        span_tree.append((parent[u], u))
        cost += dist[u]
        for v, edge_cost in graph.adjList[u]:
            if dist[v] > edge_cost:
                dist[v], parent[v] = edge_cost, u
    return span_tree[1:], cost

parent, rank = dict(), dict()

def find(u):
    parent[u] = find(parent[u]) if parent[u] != u else u
    return parent[u]

def union(u, v):
    u, v = find(u), find(v)
    if u != v:
        if rank[u] > rank[v]:
            parent[v] = u
        else:
            parent[u] = v
            if rank[u] == rank[v]:
                rank[v] += 1

def kruskal(graph):
    span_tree, cost = [], 0
    for u in graph.adjList:
        parent[u], rank[u] = u, 0
    edges = sorted([(edge_cost, (u, v)) for u in graph.adjList for v, edge_cost in graph.adjList[u] if v > u])
    for c, (u, v) in edges:
        if find(u) != find(v):
            span_tree.append((u, v))
            cost += c
            union(u, v)
    return span_tree, cost

def test():
    n, initial = 10, 0
    g = generateGraph(n)
    spTree1, cost1 = prim(g)
    spTree2, cost2 = kruskal(g)
    print(spTree1)
    print(spTree2)
    assert cost1 == cost2

test()
