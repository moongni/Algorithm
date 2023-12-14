import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

N = int(input())
self_cost = [int(input()) for _ in range(N)]
graph = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N + 1)]

edges = []
for i in range(N):
    edges.append((i, N, self_cost[i]))
    for j in range(i + 1, N):
        edges.append((i, j, graph[i][j]))
edges.sort(key=lambda x: x[2])


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
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        cost += c
        cnt += 1
        if cnt == N:
            break
print(cost)