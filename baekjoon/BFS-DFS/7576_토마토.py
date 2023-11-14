import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * M for _ in range(N)]

days = 0
queue = deque()
for y in range(N):
    for x in range(M):
        if field[y][x] == 1 and not visited[y][x]:
            visited[y][x]
            queue.append([y, x, 0])

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
while queue:
    y, x, day = queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (nx >= 0 and nx < M) and (ny >= 0 and ny < N)\
            and field[ny][nx] == 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                cur_day = day + 1
                field[ny][nx] = cur_day
                queue.append([ny, nx, cur_day])
                days = max(days, cur_day)

is_all = True
for row in range(N):
    for col in range(M):
        if field[row][col] == 0:
            is_all = False
            break
    if not is_all:
        break
if is_all:
    print(days)
else:
    print(-1)