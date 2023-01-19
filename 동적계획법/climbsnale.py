"""
    우물을 기어오르는 달팽이
    깊이 n 미터 바닥에 달팽이가 있고 끝까지 오르려고 한다.
    날씨에 따라 하루동안 올라간 높이가 변화하는데
    평소 2m 비가오면 1m 올라간다.
    m 일 동안 올라갔을 때, 달팽이가 우물을 기어올라오 올 수 있는 확률은?
"""
n = 10
m = 5

# 완전탐색
def climb_up(day, climb):
    # 기저조건: m일날 우물보다 높이 올라간 경우
    if day == m:
        if climb >= n: return 1
        else: return 0

    # 비가 안오는 경우
    return climb_up(day + 1, climb + 2) + climb_up(day + 1, climb + 1)

# print(climb_up(0, 0))


# 동적계획법
# 달팽이가 기어 올라간 날의 수를 반환
cache = [[-1 for _ in range(25)] for _ in range(25)]

def dynamic_climb_up(day, climb):
    # 기저사례 m일 안에 올라 갔는가
    if day == m:
        if climb >= n:
            return 1
        else:
            return 0

    if cache[day][climb] != -1:
        return cache[day][climb]
    
    cache[day][climb] = dynamic_climb_up(day + 1, climb + 2) + dynamic_climb_up(day + 1, climb + 1)

    return cache[day][climb]

from printBoard import print_board

# print(dynamic_climb_up(0, 0))
# print_board(cache)

"""
   같은 문제에서 비 올 확률을 75%라고 한다면
   달팽이가 기어올라 갈 수 있는 확률을 반환한다. 
"""

cache2 = [[-1 for _ in range(25)] for _ in range(25)]

def dynamic_climb_up2(day, climb):
    if day == m:
        if climb >= n:
            return 1
        else:
            return 0
    
    # 메모이제이션
    if cache2[day][climb] != -1:
        return cache2[day][climb]
    
    cache2[day][climb] = 0.25 * dynamic_climb_up2(day + 1, climb + 2) + 0.75 * dynamic_climb_up2(day + 1, climb + 1)

    return cache2[day][climb]

print(dynamic_climb_up2(0, 0))
print_board(cache2)