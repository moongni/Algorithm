import sys

input = sys.stdin.readline
INF = sys.maxsize

N, M = map(int, input().split())
board = [list(input().rstrip()) for _ in range(N)]
for i in range(1, N - 1):
    for j in range(1, M - 1):
        if board[i][j] == 'R':
            R_pos = [i, j]
        if board[i][j] == 'B':
            B_pos = [i, j]
        if board[i][j] == 'O':
            hole_pos = [i, j]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def DFS(R_pos, B_pos, move_cnt):
    if move_cnt > 9:
        return INF
    
    ret = INF
    for i in range(4):
        d = [dy[i], dx[i]]
        n_R_pos = [R_pos[0], R_pos[1]]
        n_B_pos = [B_pos[0], B_pos[1]]

        move_r, move_b = True, True
        while move_r or move_b:
            # red move
            if move_r:
                n_R_pos = [n_R_pos[0] + d[0], n_R_pos[1] + d[1]]
                if board[n_R_pos[0]][n_R_pos[1]] == '#':
                    n_R_pos = [n_R_pos[0] - d[0], n_R_pos[1] - d[1]]
                    move_r = False
                if n_R_pos == n_B_pos:
                    n_R_pos = [n_R_pos[0] - d[0], n_R_pos[1] - d[1]]
                    if not move_b:
                        move_r = False
                if board[n_R_pos[0]][n_R_pos[1]] == 'O':
                    n_R_pos = [-1, -1]
                    move_r = False
                    
            # blue move
            if move_b:
                n_B_pos = [n_B_pos[0] + d[0], n_B_pos[1] + d[1]]
                if board[n_B_pos[0]][n_B_pos[1]] == '#':
                    n_B_pos = [n_B_pos[0] - d[0], n_B_pos[1] - d[1]]
                    move_b = False
                if n_B_pos == n_R_pos:
                    n_B_pos = [n_B_pos[0] - d[0], n_B_pos[1] - d[1]]
                    if not move_r:
                        move_b = False
                if board[n_B_pos[0]][n_B_pos[1]] == 'O':
                    n_B_pos = [-1, -1]
                    move_b = False
        
        # blue escape case
        if n_B_pos[0] == -1 and n_B_pos[1] == -1:
            continue
        # only red escape case
        if n_R_pos[0] == -1 and n_R_pos[1] == -1:
            ret = min(ret, move_cnt + 1)
            continue
        # not moving case
        if R_pos == n_R_pos and B_pos == n_B_pos:
            continue
        # move next
        ret = min(ret, DFS(n_R_pos, n_B_pos, move_cnt + 1))
        
    return ret

board[R_pos[0]][R_pos[1]] = '.'
board[B_pos[0]][B_pos[1]] = '.'
ret = DFS(R_pos, B_pos, 0)
print(ret if ret != INF else -1)