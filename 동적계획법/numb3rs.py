"""
    두니발 박사의 탈옥
    매일 인접한 다른 마을로 이동할 때 n개의 도시에서 d일 후에 두니발 박사가 있을 확률을 구하여라
"""
from printBoard import print_board

# 스스로 푼 함수
def breakDay(day, p):
    # 기저조건: 탈옥 1일차 때 있을 확율을 구함
    if day == 1: 
        return get_connected_per(P, p)

    # 메모이제이션
    if cache[day][p] != -1: return cache[day][p]

    cache[day][p] = 0    

    # 현재 p 위치에 연결된 도시 인덱스
    connected = get_connected_list(p)

    for city in connected:
        cache[day][p] += breakDay(day - 1, city) * get_connected_per(city, p)
    
    return cache[day][p]

# 연결된 도시의 리스트 반환
def get_connected_list(from_):
    return [i for i in range(len(MAP[from_])) if MAP[from_][i] == 1]

def get_connected_per(from_, to):
    connected = len(get_connected_list(from_))

    if MAP[from_][to]:
        return 1 / connected
    
    return 0

# 감옥이 있는 도시 인덱스
P = 0
# 도시 연결 배열
MAP = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]
cache = [[-1 for _ in range(5)] for _ in range(4)]

print("예제 1" + "=" * 30)
print(breakDay(2, 0))
print(breakDay(2, 2))
print(breakDay(2, 4))
print(breakDay(3, 1))

P = 3
MAP = [
    [0, 1, 1, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 1, 1, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 1]
]

cache = [[-1 for _ in range(8)] for _ in range(101)]

print("예제 2" + "=" * 30)
print(breakDay(2, 3))
print(breakDay(2, 1))
print(breakDay(2, 2))
print(breakDay(2, 6))

# 답지
def breakDay2(day, here):
    # 기저조건: day가 d와 같을 때
    if (day == d): 
        if (here == q): return 1
        else: return 0

    # 메모이제이션
    if cache[day][here] != -1: return cache[day][here]

    cache[day][here] = 0

    for there in range(0, n):
        if MAP[here][there]:
            cache[day][here] += breakDay2(day + 1, there) / DEG[here]
        
    return cache[day][here]

# 도시에 연결된 수의 리스트를 반환하는 함수
def make_deg(map):
    deg = [0] * n

    for i in range(len(map)):
        for j in range(len(map[0])):
            if map[i][j] == 1:
                deg[i] += 1
    
    return deg

# n 도시의 수 / P 감옥이 있는 도시 인덱스 / d 지난 날
n = 5; P = 0; d = 2

# 도시 연결 배열
MAP = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]
# 도시에 연결된 수 리스트
DEG = make_deg(MAP)


print("예제 1" + "=" * 30)
cache = [[-1 for _ in range(5)] for _ in range(5)]
q = 0
print(breakDay2(0, P))

cache = [[-1 for _ in range(5)] for _ in range(5)]
q = 2
print(breakDay2(0, P))

cache = [[-1 for _ in range(5)] for _ in range(5)]
q = 4
print(breakDay2(0, P))

"""
    직접 풀이와 답지 차이
    1. 문제 풀이 순서를 거꾸로 생각함
    직접 풀이한 것은 날에 마지막에서 첫날로 추적해가며 확률을 계산, 답지 0일 부터 d일이 됬을 때 q도시에 도달할 확률을 계산
    장단점: 직접 풀이의 경우 day가 늘어나면 메모이제이션을 쓰기 편하지만 앞설 경우 메모이제이션을 사용하지 않을 가능성 있음
           답지 풀이의 경우 메모이제이션을 사용하기 용이하지만 각 문제에 따라 글로벌 변수를 다시 선언해야함
    
    2. 확률을 구하는 방식
    직접 풀이의 경우 확률을 반환하는 함수를 사용
    답지 풀이의 경우 도시가 연결된 리스트를 만들어 참조하여 사용 -> 답지의 경우는 메모리를 더 사용하기는 하지만 더 빠름
"""

# 2. 차이를 참조한 풀이

def breakDay3(day, here):
    # 기저조건: 0일 경우 교도소가 있는 도시인지 확인
    if day == 0:
        if here == P: return 1
        else: return 0

    # 메모이제이션
    if cache[day][here] != -1: return cache[day][here]

    cache[day][here] = 0

    for city in range(len(MAP)):
        if MAP[here][city]:
            cache[day][here] += breakDay3(day - 1, city) / DEG[city]
    return cache[day][here]

# 감옥이 있는 도시 인덱스
P = 0
# 도시 연결 배열
MAP = [
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1],
    [1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 0, 0]
]

DEG = make_deg(MAP)

cache = [[-1 for _ in range(5)] for _ in range(4)]

print("예제 1" + "=" * 30)
print(breakDay3(2, 0))
print(breakDay3(2, 2))
print(breakDay3(2, 4))
print(breakDay3(3, 1))
print_board(cache)


"""
    마르코프 연쇄
    이 문제에서 다루는 마을들은 마르코프 연쇄 라고 부르는 모델로 표현할 수 있다. 
    아래의 성격과 같다.
    1. 유한개의 상태가 있다.
    2. 매 시간마다 상태가 변경된다.
    3. 어떤 상태 a에서 다른 상태 b로 옮겨갈 확률은 현재 상태 a에만 좌우된다.
    (a 이전에 어느 상태에 있었는지, 현재 시간은 얼마인지 등은 영향을 주지 않는다.)
"""