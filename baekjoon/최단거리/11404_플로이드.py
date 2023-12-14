import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
INF = sys.maxsize

# 그래프 초기화
graph = [[INF] * N for _ in range(N)]
for i in range(N):
    graph[i][i] = 0
    
for _ in range(M):
    i, j, c = map(int, input().split())
    i -= 1
    j -= 1
    graph[i][j] = min(graph[i][j], c)

# 플로이드-워셜 알고리즘
for k in range(N):
    for i in range(N):
        for j in range(N):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(N):
    for j in range(N):
        if graph[i][j] == INF:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()