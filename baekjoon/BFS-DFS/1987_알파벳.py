import sys
input = sys.stdin.readline

R, C = map(int, input().split())
board = [list(map(lambda x: ord(x) - 65, input().rstrip())) for _ in range(R)]
alpha = [False] * 26
ret = 1

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(x, y, cnt):
    global ret
    ret = max(ret, cnt)
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # out of board
        if (nx < 0 or nx >= C) or (ny < 0 or ny >= R):
            continue
        # not duplicated path
        if not alpha[board[ny][nx]]:
            alpha[board[ny][nx]] = True
            dfs(nx, ny, cnt + 1)
            alpha[board[ny][nx]] = False

alpha[board[0][0]] = True
dfs(0, 0, ret)
print(ret)