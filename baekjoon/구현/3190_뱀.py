import sys

input = sys.stdin.readline

N = int(input())
board = [[0] * N for _ in range(N)]
board[0][0] = -1
snake = [[0, 0]]

K = int(input())
apples = [list(map(int, input().split())) for _ in range(K)]
for apple in apples:
    board[apple[0] - 1][apple[1] - 1] = 1
    
L = int(input())
moves = [input().rstrip().split() for _ in range(L)][::-1]

time = 0
direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
d_idx = 0
while True:
    h_row, h_col = snake[-1]
    # 방향 재설정 확인
    if moves and int(moves[-1][0]) == time:
        if moves[-1][1] == 'D':
            d_idx += 1
            d_idx %= 4
        else:
            d_idx -= 1
            if d_idx < 0:
                d_idx = 3
        moves.pop()
    new_row, new_col = h_row + direction[d_idx][0], h_col + direction[d_idx][1]
    time += 1
    
    # 벽에 부딪히거나 자기 몸에 걸림
    if (new_row >= N or new_row < 0) or (new_col >= N or new_col < 0) or board[new_row][new_col] == -1:
        break
    
    # 뱀 이동
    snake.append([new_row, new_col])
    if board[new_row][new_col] != 1:
        tail = snake.pop(0)
        board[tail[0]][tail[1]] = 0
    board[new_row][new_col] = -1
    
print(time)