N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

def find_square():
    max_length = min(N, M) - 1  # 최대 사각형 크기
    for step in range(max_length, -1, -1):
        for row in range(N - step):
            for col in range(M - step):
                if board[row][col] \
                    == board[row][col + step] \
                    == board[row + step][col] \
                    == board[row + step][col + step]:
                    return (step + 1) ** 2
                
print(find_square())