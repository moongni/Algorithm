import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
campus = [list(input().rstrip()) for _ in range(N)]

# I의 좌표 찾기
I = [0, 0]  # x, y
for y in range(N):
    for x in range(M):
        if campus[y][x] == 'I':
            I[0] = x
            I[1] = y
            break                

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y):
    ret = 0
    queue = deque([[x, y]])
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # campus를 벗어나거나 벽에 막힌 경우
            if (nx < 0 or nx >= M) or (ny < 0 or ny >= N) or campus[ny][nx] == 'X':
                continue
            
            # 사람을 만나는 경우
            if campus[ny][nx] == 'P':
                ret += 1
            campus[ny][nx] = 'X'
            queue.append([nx, ny])
            
    if ret == 0: 
        return 'TT'
    
    return ret

print(bfs(*I))