import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
stations = set(map(int, input().split()))
edges = []
for _ in range(M):
    u, v, w = map(int, input().split())
    u = 0 if u in stations else u
    v = 0 if v in stations else v
    edges.append((u, v, w))
edges.sort(key=lambda x: x[2])

parents = [i for i in range(N + 1)]

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
    
tot_weight = 0    
for u, v, w in edges:
    if find(u) != find(v):
        union(u, v)
        tot_weight += w

print(tot_weight)