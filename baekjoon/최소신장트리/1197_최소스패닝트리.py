import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline


V, E = map(int, input().split())
graph = defaultdict(list)
for _ in range(E):
    u, v, cost = map(int, input().split())
    graph[u].append([cost, v])
    graph[v].append([cost, u])

visited = [0] * (V + 1)
def prim(graph, node):
    queue = [[0, node]]     # cost, node idx
    total_cost = 0
    while queue:
        cost, cur_node = heapq.heappop(queue)
        if visited[cur_node] == 0:
            visited[cur_node] = 1
            total_cost += cost        
            for cost, dest in graph[cur_node]:
                if visited[dest] == 0:
                    heapq.heappush(queue, [cost, dest])
    return total_cost

print(prim(graph, 1))


### Kruskal
V, E = map(int, input().split())
parents = [i for i in range(V + 1)]
edges = [tuple(map(int, input().split())) for _ in range(E)]
graph = sorted(edges, key=lambda x: x[2])

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
        
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
    elif a > b:
        parents[a] = b
        
cost = 0
cnt = 0
for a, b, c in graph:
    if find(a) != find(b):
        union(a, b)
        cost += c
        cnt += 1
        if cnt == V - 1:
            break
print(cost)