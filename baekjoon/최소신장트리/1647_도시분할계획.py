import sys

input = sys.stdin.readline

N, M = map(int, input().split())
parents = [i for i in range(N + 1)]
edges = [list(map(int, input().split())) for _ in range(M)]
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
        
cost = m = cnt = 0
for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        cost += c
        cnt += 1
        # 가장 cost가 높은 엣지 저장
        if m < c:
            m = c
        # 모든 노드 연결
        if cnt == N - 1:
            break
print(cost - m)        