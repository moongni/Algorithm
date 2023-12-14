import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
plans = list(map(int, input().split()))

parents = [i for i in range(N+1)]

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

# 연결된 도시 union        
for i in range(N):
    for j in range(i, N):
        if graph[i][j] == 1:
            union(i+1, j+1)

# 여행 계획이 가능한지 확인
token = find(plans[0])
for i in range(1, M):
    if token != find(plans[i]):
        print('NO')
        break
else:
    print('YES')