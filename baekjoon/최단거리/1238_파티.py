import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline
INF = sys.maxsize

N, M, X = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))     # (도착지, 걸리는 시간)

# X에서 각 집까지 걸리는 시간 계산
dist_from_X = [INF] * (N + 1)
visited = [False] * (N + 1)
H = [(0, X)]
while H:
    cost, curr = heapq.heappop(H)
    visited[curr] = True
    dist_from_X[curr] = min(dist_from_X[curr], cost)

    for next, c in graph[curr]:
        if not visited[next]:
            heapq.heappush(H, (cost + c, next))

# 각 집에서 X까지 걸리는 시간 
dist_to_X = [INF] * (N + 1)
for i in range(1, N + 1):
    visited = [False] * (N + 1)
    H = [(0, i)]
    while H:
        cost, curr = heapq.heappop(H)
        visited[curr] = True
        if curr == X:
            dist_to_X[i] = cost
            break
        for next, c in graph[curr]:
            if not visited[next]:
                heapq.heappush(H, (cost + c, next))

max_dist = 0
for i in range(1, N + 1):
    dist = dist_to_X[i] + dist_from_X[i]
    max_dist = max(max_dist, dist)
    
print(max_dist)