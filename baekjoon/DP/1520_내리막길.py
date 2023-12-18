import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

M, N = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(M)]
dp = [[-1] * N for _ in range(M)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def get_path(x, y):
    if x == N - 1 and y == M - 1:
        return 1
    
    if dp[y][x] != -1:
        return dp[y][x]
    
    dp[y][x] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (nx >= 0 and nx < N) and (ny >= 0 and ny < M) \
            and maps[ny][nx] < maps[y][x]:
                dp[y][x] += get_path(nx, ny)
    return dp[y][x]

print(get_path(0, 0))