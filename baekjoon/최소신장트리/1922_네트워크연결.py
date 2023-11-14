import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
connections = [tuple(map(int, input().split())) for _ in range(M)]

# prim
from collections import defaultdict
import heapq

visited = [0] * (N + 1)
graph = defaultdict(list)
for src, dest, cost in connections:
    graph[src].append([cost, dest])
    graph[dest].append([cost, src])

def prim(graph, node=1):
    queue = [[0, node]]
    total_cost = 0
    while queue:
        cost, node = heapq.heappop(queue)
        if visited[node] == 0:
            visited[node] = 1
            total_cost += cost
            
            for c, n in graph[node]:
                if visited[n] == 0:
                    heapq.heappush(queue, [c, n])
    return total_cost

print(prim(graph))

# Kruskal
parents = [i for i in range(N + 1)]
graph = sorted(connections, key=lambda x: x[2])

def find(x):
    if parents[x] == x:
        return x
    else:
        parents[x] = find(parents[x])
        return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[a] = b
    elif a > b:
        parents[b] = a

cost = 0
cnt = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        cost += c
        cnt += 1

        if cnt == N - 1:
            break
print(cost)
