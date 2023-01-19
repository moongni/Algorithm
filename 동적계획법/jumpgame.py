from printBoard import print_board
"""
    점핑 게임
    
    규칙
    1부터 9까지 수가 적힌 n x n 보드가 있다.
    왼쪽 위에서 오른쪽 아래까지 이동을 하는데 현재 위치에 적힌 숫자만큼 아래나 오른쪽으로 이동할 수 있다.
    보드 바깥으로 나갈 수 없다.

"""

BOARD = [
    [2,5,1,6,1,4,1],
    [6,1,1,2,2,9,3],
    [7,2,3,2,1,3,1],
    [1,1,3,1,7,1,2],
    [4,1,2,3,4,1,2],
    [3,3,1,2,3,4,1],
    [1,5,2,9,4,7,-1]
]


# 재귀를 이용한 완전탐색기법
def recursive_jg(y, x):
    # 기저 조건 보드 밖으로 나가는 경우
    if y >= len(BOARD) or x >= len(BOARD[0]):
        return 0
    
    # 기저 조건 오른쪽 끝에 다달은 경우
    if y == len(BOARD) - 1 and x == len(BOARD) - 1:
        return 1
    
    # 현재 보드 숫자
    jp = BOARD[y][x]

    # 우측 또는 하단 이동
    return recursive_jg(y, x + jp) or recursive_jg(y + jp, x)

print(recursive_jg(0,0))

# 동적 계획법을 이용
cache = [[-1 for _ in range(len(BOARD))] for _ in range(len(BOARD[0]))]

def dynamic_jg(y, x):
    # 기저 조건 보드 밖으로 나가는 경우
    if y >= len(BOARD) or x >= len(BOARD[0]):
        return 0
    # 기저 조건 오른쪽 끝에 다달은 경우
    if y == len(BOARD) - 1 and x == len(BOARD) - 1:
        cache[y][x] = 1
        return 1
    
    # 캐시 확인
    if cache[y][x] != -1:
        return cache[y][x]
            
    jp = BOARD[y][x]

    cache[y][x] = dynamic_jg(y, x + jp) or dynamic_jg(y + jp, x)
    
    return cache[y][x]

print(dynamic_jg(0, 0))
print_board(cache)