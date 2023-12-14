import sys
from collections import defaultdict
import heapq

input = sys.stdin.readline
INF = 1000 * 2000 + 1

T = int(input())

def dijkstra(s):
    distance = [INF] * (n + 1)
    distance[s] = 0
    H = [(0, s)]    # distance, start
    while H:
        dist, curr = heapq.heappop(H)
        for dest, d in graph[curr]:
            new_dist = dist + d
            if new_dist < distance[dest]:
                distance[dest] = new_dist
                heapq.heappush(H, (new_dist, dest))
    return distance

for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = defaultdict(list)
    for _ in range(m):
        a, b, d = map(int, input().split())
        graph[a].append((b, d)) # dest, dist
        graph[b].append((a, d))
        
    candidate = [int(input()) for _ in range(t)]
    candidate.sort()
    
    # s에서 모든 거리 확인
    dist_from_s = dijkstra(s)
    
    # 흔적 중 더 먼 노드에서 candidate까지 거리 확인 
    k = h if dist_from_s[g] < dist_from_s[h] else g
    dist_from_k = dijkstra(k)

    for cand in candidate:
        if dist_from_s[cand] == dist_from_s[k] + dist_from_k[cand]:
            print(cand, end=' ')