import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

N, M = map(int, input().split())

maps = [list(input().rstrip()) for _ in range(N)]

def dfs(x, y):
    global maps
    tile = maps[y][x]
    maps[y][x] = '.'
    if tile == '-' :    # 가로
        if x + 1 < M and maps[y][x + 1] == tile:
            dfs(x + 1, y)
    else:               # 세로
        if y + 1 < N and maps[y + 1][x] == tile:
            dfs(x, y + 1)
    
ret = 0
for row in range(N):
    for col in range(M):
        if maps[row][col] != '.':
            dfs(col, row)
            ret += 1

print(ret)