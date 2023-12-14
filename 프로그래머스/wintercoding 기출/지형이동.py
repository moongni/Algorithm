import heapq
from collections import defaultdict
import sys


def solution(land, height):
    N = len(land)
    graph = defaultdict(list)
    
    # 그래프 생성
    dx = [1, 0]
    dy = [0, 1]
    for y in range(N):
        for x in range(N):
            for i in range(2):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx >= N or ny >= N:
                    continue
                diff = abs(land[y][x] - land[ny][nx])
                diff = 0 if diff <= height else diff
                graph[f'{y} {x}'].append([diff, (y, x), (ny, nx)])
                graph[f'{ny} {nx}'].append([diff, (ny, nx), (y, x)])
    return prim(graph, N, 0, 0)

def prim(graph, N, y, x):
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    candidate = graph[f'{y} {x}']
    heapq.heapify(candidate)
    mst = []
    total_weight = 0
    
    while candidate:
        weight, u, v = heapq.heappop(candidate)
        if visited[v[0]][v[1]] == 0:
            visited[v[0]][v[1]] = 1
            mst.append((u, v))
            total_weight += weight
            
            for edge in graph[f'{v[0]} {v[1]}']:
                if visited[edge[2][0]][edge[2][1]] == 0:
                    heapq.heappush(candidate, edge)
    return total_weight
    