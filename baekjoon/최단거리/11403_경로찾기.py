import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

connected = [[0] * N for _ in range(N)]
for i in range(N):
    queue = deque([i])
    while queue:
        curr = queue.popleft()
        for j in range(N):
            if graph[curr][j] == 1 and not connected[i][j]:
                queue.append(j)
                connected[i][j] = 1

for row in connected:
    print(' '.join(map(str, row)))