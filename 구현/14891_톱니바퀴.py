"""덱 활용"""
import sys
from collections import deque

input = sys.stdin.readline
gears = []
for _ in range(4):
    gears.append(deque(list(input().rstrip())))
K = int(input())
turns = [list(map(int, input().split())) for _ in range(K)]

def rotate_gear(gear: deque, toward):
    """기어를 회전시키는 함수"""
    if toward == 1:
        gear.appendleft(gear.pop())
    else:
        gear.append(gear.popleft())

l_idx, r_idx = 6, 2
for i, to in turns:
    i -= 1  # reindexing
    left, right = gears[i][l_idx], gears[i][r_idx]
    # 현재 기어 회전
    rotate_gear(gears[i], to)
    
    # 기준 왼쪽 회전
    l_gear, cur_gear = i - 1, i
    turn_to = to
    while l_gear >= 0:
        # 같은 극일 경우 회전하지 않고 탈출
        if gears[l_gear][r_idx] == left:
            break
        # 다른 극일 경우 반대로 회전
        left = gears[l_gear][l_idx]
        turn_to = -turn_to
        rotate_gear(gears[l_gear], turn_to)
        l_gear -= 1
        cur_gear -= 1
    # 기준 오른쪽 회전
    r_gear, cur_gear = i + 1, i
    turn_to = to
    while r_gear <= 3:
        # 같은 극일 경우 회전하지 않고 탈출
        if right == gears[r_gear][l_idx]:
            break
        # 다른 극일 경우 반대로 회전
        right = gears[r_gear][r_idx]        
        turn_to = -turn_to
        rotate_gear(gears[r_gear], turn_to)
        r_gear += 1
        cur_gear += 1
    
ret = 0
for i in range(4):
    ret += int(gears[i][0]) * 2**i
print(ret)

"""list 활용"""
import sys

input = sys.stdin.readline
gears = []
for _ in range(4):
    gears.append(list(input().rstrip()))
K = int(input())
turns = [list(map(int, input().split())) for _ in range(K)]

def rotate_gear(gear, toward):
    """기어를 회전시키는 함수"""
    if toward == 1:
        gear.insert(0, gear.pop())
    else:
        gear.append(gear.pop(0))
    return gear

l_idx, r_idx = 6, 2
for i, to in turns:
    i -= 1  # reindexing
    left, right = gears[i][l_idx], gears[i][r_idx]
    # 현재 기어 회전
    gears[i] = rotate_gear(gears[i], to)
    
    # 기준 왼쪽 회전
    l_gear, cur_gear = i - 1, i
    turn_to = to
    while l_gear >= 0:
        # 같은 극일 경우 회전하지 않고 탈출
        if gears[l_gear][r_idx] == left:
            break
        # 다른 극일 경우 반대로 회전
        left = gears[l_gear][l_idx]
        turn_to = -turn_to
        gears[l_gear] = rotate_gear(gears[l_gear], turn_to)
        l_gear -= 1
        cur_gear -= 1
    # 기준 오른쪽 회전
    r_gear, cur_gear = i + 1, i
    turn_to = to
    while r_gear <= 3:
        # 같은 극일 경우 회전하지 않고 탈출
        if right == gears[r_gear][l_idx]:
            break
        # 다른 극일 경우 반대로 회전
        right = gears[r_gear][r_idx]        
        turn_to = -turn_to
        gears[r_gear] = rotate_gear(gears[r_gear], turn_to)
        r_gear += 1
        cur_gear += 1
    
ret = 0
for i in range(4):
    ret += int(gears[i][0]) * 2**i
print(ret)