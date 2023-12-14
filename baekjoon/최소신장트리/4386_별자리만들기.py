import sys
from collections import defaultdict
import heapq
import math

input = sys.stdin.readline

N = int(input())
stars = [list(map(float, input().split())) for _ in range(N)]
graph = defaultdict(list)

def get_dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def prim():
    cost = 0
    cnt = 0
    H = [(0, 0)] # cost, node
    while H:
        c, node = heapq.heappop(H)
        if not visited[node]:
            visited[node] = True
            cost += c
            cnt += 1
            for c, dst in graph[node]:
                if not visited[dst]:
                    heapq.heappush(H, (c, dst))
        
    return cost

for i in range(N - 1):
    for j in range(i + 1, N):
        dist = get_dist(stars[i], stars[j])
        # dist, destination
        graph[i].append((dist, j))
        graph[j].append((dist, i))
        
visited = [False] * N
print(f"{prim():0.02f}")