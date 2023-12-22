import sys

input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]

def DFS(row):
    if row == N:
        return 1
    
    ret = 0
    for col in range(N):
        flag = True
        # check
        for j in range(1, row + 1):
            if board[row - j][col] == 1:
                flag = False
                break
            if j <= col and board[row - j][col - j] == 1:
                flag = False
                break
            if j <= N - col - 1 and board[row - j][col + j] == 1:
                flag = False
                break
                            
        if flag:
            board[row][col] = 1
            ret += DFS(row + 1)
            board[row][col] = 0
    return ret

print(DFS(0))