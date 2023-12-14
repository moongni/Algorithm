import sys
import math

input = sys.stdin.readline

N, M = map(int, input().split())
nodes = [list(map(int, input().split())) for _ in range(N)]
connected = [list(map(int, input().split())) for _ in range(M)]

# kruskal을 위한 변수 선언
parents = [i for i in range(N)]
edges = []

def get_dist(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

cnt = 0
def union(a, b):
    global cnt
    a, b = find(a), find(b)
    if a < b:
        parents[b] = a
        cnt += 1
    elif a > b:
        parents[a] = b
        cnt += 1
    

# 각 우주인 별 가중치 계산
for i in range(N - 1):
    for j in range(i + 1, N):
        edges.append([i, j, get_dist(nodes[i], nodes[j])])
edges.sort(key=lambda x: x[2])

cost = 0
# 이미 연결된 노드 계산
for a, b in connected:
    union(a - 1, b - 1)
    
# kruskal 실행
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        cost += c
        if cnt == N - 1:
            break
    
print(f"{round(cost, 2):0.02f}")