import sys
from itertools import combinations

input = sys.stdin.readline
N, M = map(int, input().split())
chickens = []
homes = []

# 입력을 치킨집 위치 배열과 가정집 위치 배열로 받음
for r in range(N):
    cities = input().split()
    for c in range(len(cities)):
        if cities[c] == '1':
            homes.append((r, c))
        elif cities[c] == '2':
            chickens.append((r, c))

def get_dist(homes, chickens):
    ret = sys.maxsize   # 최소 거리 저장 변수
    for chicken in combinations(chickens, M):   # 가능한 치킨 집 조합
        cur_dist = 0
        for h in homes: # 각 집을 순회하며 치킨집과의 최소거리 구함
            dist = sys.maxsize 
            for c in chicken: 
                dist = min(dist, abs(c[0] - h[0]) + abs(c[1] - h[1]))
            cur_dist += dist
        ret = min(ret, cur_dist)
    return ret

print(get_dist(homes, chickens))