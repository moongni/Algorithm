# 미해결

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
maps = [[-1 if m else 0 for m in map(int, list(input().rstrip()))] for _ in range(N)]

INF = (10 ** 6)
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(cur_x, cur_y, is_break=False):
    queue = deque([[cur_x, cur_y, maps[cur_y][cur_x]]])
    ret = INF    
    while queue:
        x, y, cost = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            cur_cost = cost + 1
            
            if (nx < 0 or nx >= M) or (ny < 0 or ny >= N) or (maps[ny][nx] > 0 and maps[ny][nx] < cur_cost):
                continue

            if maps[ny][nx] == -1 and not is_break:
                # print(ny, nx, 'break')
                maps[ny][nx] = cur_cost
                ret = min(ret, bfs(nx, ny, True))
                maps[ny][nx] = -1
            elif maps[ny][nx] != -1:
                maps[ny][nx] = cur_cost
                queue.append([nx, ny, cur_cost])
    # for row in maps:
    #     print(' '.join(list(map(str, row))))
    return min(ret, maps[N - 1][M - 1])        

maps[0][0] = 1
cost = bfs(0, 0)
print(cost if cost != 0 else -1)