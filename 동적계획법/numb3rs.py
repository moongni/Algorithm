"""
    두니발 박사의 탈옥
    매일 인접한 다른 마을로 이동할 때 n개의 도시에서 d일 후에 두니발 박사가 있을 확률을 구하여라
"""

def breakDay(day, p):
    if day == 1: 
        return get_connected_per(P, p)

    if cache[day][p] != -1: return cache[day][p]

    cache[day][p] = 0    

    connected_list = get_connected_list(p)

    for city in connected_list:
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
cache = [[-1 for _ in range(5)] for _ in range(101)]

print(breakDay(2, 0))
print(breakDay(2, 2))
print(breakDay(2, 4))

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

print(breakDay(2, 3))
print(breakDay(2, 1))
print(breakDay(2, 2))
print(breakDay(2, 6))