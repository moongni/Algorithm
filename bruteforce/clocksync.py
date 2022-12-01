"""
    시계 맞추기 문제 - 완전 탐색
    16개의 시계는 12, 3, 6, 9 중 하나를 가르키고 있다.
    10개의 스위치는 각 연결된 시계를 3만큼 변화시킨다.
    16개의 시계가 모두 12시를 가르키게 하도록 스위치를 누르는 가장 적은 개수를 찾아라.

    열결된 시계 스위치
    0 - 0 1 2
    1 - 3 7 9 11
    2 - 4 10 14 15
    3 - 0 4 5 6 7
    4 - 6 7 8 10 12
    5 - 0 2 14 15
    6 - 3 14 15
    7 - 4 5 7 14 15
    8 - 1 2 3 4 5
    9 - 3 4 5 9 13
"""

SWITCH = {
    0 : [0, 1, 2],
    1 : [3, 7, 9, 11],
    2 : [4, 10, 14, 15],
    3 : [0, 4, 5, 6, 7],
    4 : [6, 7, 8, 10, 12],
    5 : [0, 2, 14, 15],
    6 : [3, 14, 15],
    7 : [4, 5, 7, 14 ,15],
    8 : [1, 2, 3, 4 ,5],
    9 : [3, 4, 5, 9 ,13],
}

# 모든 시계가 12시를 가르키는 지 확인하는 함수
def check_12(clocks):
    for time in clocks:
        if time != 12:
            return False
    
    return True

# 스위치를 누르면 시계를 움직이는 함수
def push(clocks, switch):
    for clock in SWITCH[switch]:
        clocks[clock] += 3
        # 시계가 12시를 넘은 경우
        if clocks[clock] == 15:
            clocks[clock] = 3

    
# 가장 적은 스위치의 수를 찾는 함수
def least_switch(clocks, n_switch):
    # 기저함수: 
    if n_switch == len(SWITCH):
        if check_12(clocks):
            return 0
        else: return float("inf")

    ret = float("inf")

    for i in range(4):
        ret = min(ret, i + least_switch(clocks, n_switch + 1))
        push(clocks, n_switch)

    return ret

CLOCK = [12,6,6,6 ,6,6,12,12, 12,12,12,12, 12,12,12,12]
CLOCK2 = [12,9,3,12, 6,6,9,3, 12,9,12,9, 12,12,6,6]

print(least_switch(CLOCK, 0))
print(least_switch(CLOCK2, 0))