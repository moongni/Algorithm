"""
    삼각형 위의 최대 경로
    
    6
    1 2
    3 7 4
    9 4 1 7
    2 7 5 9 4

    위와 같이 삼각형으로 배치된 자연수들이 있을 때
    한칸씩 아래로 내려가 맨 아랫 줄까지 닿는 경로를 만든다.
    아래 또는 오른쪽 아래 숫자로 내려갈 때 값을 최대화하는 경로는 무엇인가
"""

TRIANGLE = [
    [6],
    [1, 2],
    [3, 7, 4],
    [9, 4, 1, 7],
    [2, 7, 5, 9, 4]
]

def recursive_triangle_path(y, x, sum=0):
    # 기저사례: 삼각형 범위 안에 있는지 확인
    if x >= len(TRIANGLE[y]):
        return sum

    # 기저사례: 맨 아랫줄 도착
    if y == len(TRIANGLE) - 1:
        return sum + TRIANGLE[y][x]    

    # 현재 위치 추가
    sum += TRIANGLE[y][x]

    return max(recursive_triangle_path(y + 1, x, sum), recursive_triangle_path(y + 1, x + 1, sum))

# print(recursive_triangle_path(0,0))

cache = [[-1 for _ in range(len(TRIANGLE))] for _ in range(len(TRIANGLE))]

def dynamic_triangle_path(y, x, sum=0):
    # 기저사례: 삼각형 범위 안에 있는지 확인
    if x >= len(TRIANGLE[y]):
        return sum
    
    # 기저사례: 맨 아랫줄 도착
    if y == len(TRIANGLE) - 1:
        cache[y][x] = sum + TRIANGLE[y][x]
        return cache[y][x]
    
    # 캐싱된 데이터 참조
    if cache[y][x] != -1:
        return cache[y][x]

    sum += TRIANGLE[y][x]

    cache[y][x] = max(dynamic_triangle_path(y+1, x, sum), dynamic_triangle_path(y+1, x+1, sum))

    return cache[y][x]

def print_board(board):
    for row in board:
        for col in row:
            if col < 0:
                print(f"{col} ", end='')
            else:
                print(f" {col} ", end='')
        print()

# print(dynamic_triangle_path(0, 0))
# print_board(cache)

# 뒤 dynamic_triangle_path의 경우
# 경로의 합이 매번 다른 경우 계산이 반복되는 일이 없어 메모이제이션 기법을 사용해도 완전탐색기법과 다르지 않다.
# 알고리즘을 더 빠르게 만들기 위해 재귀함수의 sum을 입력받지 않아 이전까지 어떤 숫자를 만났는지 알 수 없기 때문에 
# 전체 경로의 최대 합을 반환할 수 없다.
# 따라서 함수의 반환 값을 전체 경로의 최대치가 아니라 (y, x)에서 시작하는 부분 경로의 최대치로 변화시킨다.
def dynamic_triangle_path2(y, x):
    # 기저사례 보드를 벗어나는 경우
    if x >= len(TRIANGLE[y]):
        return 0
    
    # 기저사례 맨 아랫줄 도착
    if y == len(TRIANGLE) - 1:
        cache[y][x] = TRIANGLE[y][x]
        return TRIANGLE[y][x]

    # 기저사례 메모이제이션
    if cache[y][x] != -1:
        return cache[y][x]

    cache[y][x] = max(dynamic_triangle_path2(y + 1, x), dynamic_triangle_path2(y + 1, x + 1)) + \
        TRIANGLE[y][x]
    
    return cache[y][x]

print(dynamic_triangle_path2(0, 0))
print_board(cache)
