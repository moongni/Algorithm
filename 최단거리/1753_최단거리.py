import sys
from collections import defaultdict

input = sys.stdin.readline

V, E = map(int, input().split())
start = int(input()) - 1

graph = defaultdict(list)
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u - 1].append([v - 1, w])

INF = int(1e9)
distance = [INF] * V
visited = [False] * V
def dijkstra():
    distance[start] = 0
    visited[start] = True
    for v, w in graph[start]:
        distance[v] = min(distance[v], w)    
        
    for _ in range(V - 1):
        now = get_smallest_node()
        visited[now] = True
        for v, w in graph[now]:
            cost = distance[now] + w
            if cost < distance[v]:
                distance[v] = cost

def get_smallest_node():
    min_value = INF
    index = 0
    for i in range(V):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index = i
    return index

dijkstra()

for w in distance:
    print(w if w != INF else 'INF')