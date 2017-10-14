import random
from collections import *

class Graph:
    def __init__(self):
        self.adjList = defaultdict(list)

    def add_edge(self, from_node, to_node, distance):
        self.adjList[from_node].append((to_node, distance))
        self.adjList[to_node].append((from_node, distance))

class PriorityQueue:
    def __init__(self):
        self.queue = []
        # Remember the index of the node in the priority queue
        self.indexInQueue = {}
        self.size = 0

    def __len__(self):
        return len(self.queue)

    def hasNode(self, node):
        return node in self.indexInQueue

    def getCost(self, node):
        return self.queue[self.indexInQueue[node]][0]

    def swap(self, pos1, pos2):
        self.queue[pos1], self.queue[pos2] = self.queue[pos2], self.queue[pos1]
        self.indexInQueue[self.queue[pos1][1]], self.indexInQueue[self.queue[pos2][1]] = pos1, pos2

    def update(self, node, cost):
        pos = self.indexInQueue[node]
        self.queue[pos][0] = cost
        while pos > 0:
            new_pos = (pos - 1) // 2
            if self.queue[new_pos][0] <= cost:
                break
            else:
                self.swap(new_pos, pos)
                pos = new_pos

    def push(self, node, cost):
        self.size += 1
        self.queue.append([cost, node])
        self.indexInQueue[node] = self.size - 1
        self.update(node, cost)

    def pop(self):
        # Move the last node to the first place.
        cost, node = self.queue[0]
        self.queue[0] = self.queue[-1]
        self.indexInQueue[self.queue[0][1]] = 0

        # Remove the node from the list
        del self.indexInQueue[node]
        self.queue.pop()
        self.size -= 1

        # Maintain the min-heap structure
        pos = 0
        while pos < self.size:
            # the node with smallest cost is among pos, left and right.
            left, right = pos*2, pos*2+1
            min_pos = left if left < len(self.queue) and self.queue[pos] > self.queue[left] else pos
            min_pos = right if right < len(self.queue) and self.queue[min_pos] > self.queue[right] else min_pos
            if min_pos == pos:
                break
            else:
                self.swap(pos, min_pos)
                pos = min_pos
        return [cost, node]

    def __str__(self):
        return str(self.queue) + '\n' + str(self.indexInQueue)

def generateGraph(n, threshold = 1, low = 10, high = 100):
    g = Graph()
    for i in range(n):
        for j in range(i+1, n):
            if random.uniform(0, 1) <= threshold:
                g.add_edge(i, j, random.randint(low, high))
    return g

def dijkstra(graph, initial):
    INF = float('inf')
    q = PriorityQueue()
    q.push(initial, 0)
    for u in graph.adjList:
        if u != initial:
            q.push(u, INF)
    distance = {}
    while q.size > 0:
        cost, u = q.pop()
        distance[u] = cost
        for v, edge_cost in graph.adjList[u]:
            if q.hasNode(v) and q.getCost(v) > cost + edge_cost:
                q.update(v, cost + edge_cost)
    return distance

def test_dijkstra():
    n, initial = 100, 0
    g = generateGraph(n)
    distance = dijkstra(g, initial)
    for u in g.adjList:
        for v, edge_cost in g.adjList[u]:
            assert distance[v] <= distance[u] + edge_cost

def test_priorityQueue():
    q = PriorityQueue()
    list = set([random.randint(1, 100) for _ in range(100)])
    for item in list:
        q.push('a'+str(item),item)
    ans = []
    while q.size > 0:
        ans.append(q.pop()[0])
    assert ans == sorted(ans)

test_priorityQueue()
test_dijkstra()
