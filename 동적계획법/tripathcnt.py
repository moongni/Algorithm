from printBoard import print_board
"""
    삼각형 위의 최대 경로 개수 세기
    trianglepath.py 처럼 삼각형에서 아래와 아래 오른쪽 칸을 선택할 수 있으며,
    경로의 합이 최대인 경로 개수를 반환한다.
"""
TRIANGLE = [
    [9],
    [5, 7],
    [1, 3, 2],
    [3, 5, 5, 6]
]

max_cache = [[-1 for _ in range(4)] for _ in range(4)] 

# 동적 계획법으로 삼각형 최대 합 구하기
def tri_path(y, x):
    # 삼각형 맨 아래 도착
    if y == len(TRIANGLE) - 1:
        max_cache[y][x] = TRIANGLE[y][x]
        return max_cache[y][x]
    
    # 메모이제이션
    if max_cache[y][x] != -1:
        return max_cache[y][x]
    
    # 가장 큰 합 찾기
    max_cache[y][x] = max(tri_path(y + 1, x), tri_path(y + 1, x + 1)) + TRIANGLE[y][x]

    return max_cache[y][x]

print(tri_path(0, 0))
print_cache(max_cache)

# 최대 합 경로 세기
cnt_cache = [[-1 for _ in range(4)] for _ in range(4)]
def tri_path_cnt(y, x):
    # 기저조건: 열의 마지막 줄인 경우
    if y == len(TRIANGLE) - 1:
        cnt_cache[y][x] = 1
        return 1

    if cnt_cache[y][x] != -1:
        return cnt_cache[y][x]

    cnt_cache[y][x] = 0

    # 판단
    # cache의 최대 합의 아래와 아래 오른쪽을 비교하여
    # 같으면 아래 두 경로의 합, 한쪽이 크면 그 경로의 값
    if max_cache[y+1][x] >= max_cache[y+1][x+1]:
        cnt_cache[y][x] += tri_path_cnt(y+1, x)
    if max_cache[y + 1][x] <= max_cache[y + 1][x + 1]:
        cnt_cache[y][x] += tri_path_cnt(y+1, x+1)
    
    return cnt_cache[y][x]

print(tri_path_cnt(0, 0))
print_cache(cnt_cache)