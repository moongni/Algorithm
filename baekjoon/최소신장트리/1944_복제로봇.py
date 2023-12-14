import sys
from collections import deque


input = sys.stdin.readline

N, M = map(int, input().split())

# 미로를 입력 받고 S, K 가 있는 좌표를 저장
maze = []
nodes = []
for i in range(N):
    string = list(input().rstrip())
    maze.append(string)
    for j in range(N):
        if string[j] in ['S', 'K']:
            nodes.append((i, j))

# bfs를 통해 S, K가 연결된 edge를 계산
edges = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
for i in range(len(nodes)):
    y, x = nodes[i]
    visited = [[0] * N for _ in range(N)]
    visited[y][x] = 1
    queue = deque([[y, x, 0]])
    while queue:
        y, x, cost = queue.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if maze[ny][nx] == '1' or visited[ny][nx]:
                continue
            if maze[ny][nx] in ['S', 'K']:
                edges.append((i, nodes.index((ny, nx)), cost + 1))
            elif maze[ny][nx] == '0':
                queue.append((ny, nx, cost + 1))
            visited[ny][nx] = 1

# kruskal 알고리즘을 통해 최소 스패닝 트리 계산
edges.sort(key=lambda x: x[2])

parents = [i for i in range(M + 1)]
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
    
tot_cost = 0
cnt = 0    
for u, v, c in edges:
    if find(u) != find(v):
        union(u, v)
        tot_cost += c
        cnt += 1
        if cnt == M:
            print(tot_cost)
            break
else:
    print(-1)