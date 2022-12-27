"""
    쿼드트리 뒤집기
    쿼드트리 주어진 공간을 4개로 분할해 재귀적으로 표현한다.
    흑백사진 압축에서 자주 사용되며
    2^n x 2^n 크기의 흑백 그림을 다음 규칙으로 압축한다.
    1. 모든 픽셀이 겁은 색 => b
    2. 모든 픽셀이 하얀 색 => w
    3. 모든 픽셀이 같은 색이 아니라면 가로 세로 2등분해 4개의 조각으로 쪼갠뒤 각각 쿼드트리 압축
       이때 전체 그림 압축결과는 x(왼쪽 위)(우측 위)(왼쪽 아래)(오른쪽 아래)

    16x16 흑백 그림을 압축한 쿼드트리가 있을 때, 상하로 뒤집은 쿼드트리를 반환하라
    1. 압축을 해제한 후 뒤집고 다시 압축하기
    2. 압축을 다 풀지 않고 뒤집기
"""

# 쿼드트리 압축
def compress(board, y, x, size):
    head = check_head(board, y, x, size)
    if head == 'b' or head == 'w':
        return head
    # 4개의 조각으로 쪼갠 뒤 재귀
    else:
        half = size // 2
        upper_left = compress(board, y, x, half)
        upper_right = compress(board, y, x + half, half)
        lower_left = compress(board, y + half, x, half)
        lower_right = compress(board, y + half, x + half, half)
    
    return 'x' + upper_left + upper_right + lower_left + lower_right

# 입력된 보드의 글자 체크
def check_head(board, y, x, size):
    head = board[y][x]

    for i in range(y, y + size):
        for j in range(x, x + size):
            if board[i][j] != head:
                return 'x'

    return head

def print_board(board):
    for row in board:
        print(row)

# 쿼드트리 압축해제
def decompress(it, y, x, size, board=None):
    if not(board):
        board = [['' for _ in range(size)] for _ in range(size)]
    
    head = it.pop(0)
    if head == 'b' or head == 'w':
        for i in range(y, y + size):
            for j in range(x, x + size):
                board[i][j] = head
    else:
        half = size // 2
        decompress(it, y, x, half, board)
        decompress(it, y, x + half, half, board)
        decompress(it, y + half, x, half, board)
        decompress(it, y + half, x + half, half, board)

    return board

# 1. 압축을 해제한 후 뒤집고 다시 압축하기
def reverse1(board: str, size: int) -> str:
    list_board = decompress(list(board), 0, 0, size)

    list_board.reverse()

    return compress(list_board, 0, 0, size)

print(reverse1('w', 16))
print(reverse1('xbwwb', 16))
print(reverse1('xbwxwbbwb', 16))
print(reverse1('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb', 16))

# 2. 압축을 하지 않고 뒤집기
def reverse2(it):
    head = it.pop(0)
    
    if head == 'b' or head == 'w':
        return head
    else:
        upperLeft = reverse2(it)
        upperRight = reverse2(it)
        lowerLeft = reverse2(it)
        lowerRight = reverse2(it)

    return 'x' + lowerLeft + lowerRight + upperLeft + upperRight

print(reverse2(list('w')))
print(reverse2(list('xbwwb')))
print(reverse2(list('xbwxwbbwb')))
print(reverse2(list('xxwwwbxwxwbbbwwxxxwwbbbwwwwbb')))
