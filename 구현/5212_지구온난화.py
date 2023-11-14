import sys
from copy import deepcopy

input = sys.stdin.readline

R, C = map(int, input().split())
maps = [list(input().rstrip()) for _ in range(R)]
maps_ = deepcopy(maps)

# 순회하며 땅이 50년 후에도 남아 있을 지 확인
for row in range(R):
    for col in range(C):
        if maps[row][col] == 'X':
            # 상하좌우에 3개 이상의 바다가 있는지 확인
            cnt = 0
            if row - 1 < 0 or maps[row - 1][col] == '.':    # 상
                cnt += 1
            if row + 1 >= R or maps[row + 1][col] == '.':   # 하 
                cnt += 1
            if col - 1 < 0 or maps[row][col - 1] == '.':    # 좌
                cnt += 1
            if col + 1 >= C or maps[row][col + 1] == '.':   # 우
                cnt += 1
            if cnt >= 3:
                maps_[row][col] = '.'

# 육지를 포함한 가장 작은 사각형 찾기
min_row, max_row = R - 1, 0
min_col, max_col = C - 1, 0
for row in range(R):
    all_sea = True
    for col in range(C):
        if maps_[row][col] == 'X':
            all_sea = False
            if min_col > col:
                min_col = col
            if max_col < col:
                max_col = col            
    if not all_sea:
        if min_row > row:
            min_row = row
        if max_row < row:
            max_row = row

for row in range(min_row, max_row + 1):
    for col in range(min_col, max_col + 1):
        print(maps_[row][col], end="")
    print()