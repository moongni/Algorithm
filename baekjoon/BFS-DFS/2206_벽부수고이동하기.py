import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(cur_x, cur_y):
    queue = deque([(cur_x, cur_y, 0)])   # x, y, is_break
    while queue:
        x, y, is_break = queue.popleft()

        if x == M - 1 and y == N - 1:
            return visited[y][x][is_break] + 1
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # out of maps
            if (nx < 0 or nx >= M) or (ny < 0 or ny >= N):
                continue
            # meet a wall and havn't broken a wall before
            if maps[ny][nx] == 1 and not is_break:
                visited[ny][nx][1] = visited[y][x][0] + 1
                queue.append((nx, ny, 1))
            # no wall and havn't visited
            elif maps[ny][nx] == 0 and not visited[ny][nx][is_break]:
                visited[ny][nx][is_break] = visited[y][x][is_break] + 1
                queue.append((nx, ny, is_break))
    return -1

print(bfs(0, 0))