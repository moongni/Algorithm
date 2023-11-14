import sys

sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
max_length = 0
strings = []
favorite = {}
for _ in range(K):
    string = input().rstrip()
    strings.append(string)
    favorite[string] = 0
    max_length = max(max_length, len(string))
    
dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]    
def dfs(x, y, string):
    # 현재 단어가 존재하는 경우    
    if favorite.get(string) is not None:
        favorite[string] += 1

    # base case: 최대 단어 길이를 초과하는 경우
    if len(string) == max_length:
        return
    
    # 8방향 탐색
    for i in range(8):
        nx = (x + dx[i]) % M
        ny = (y + dy[i]) % N
        dfs(nx, ny, string + board[ny][nx])

for i in range(N):
    for j in range(M):
        dfs(j, i, board[i][j])
        
for string in strings:
    print(favorite[string])