import sys
input = sys.stdin.readline

# 완전 탐색
def sol_brute(houses):
    ret = None
    dist = sys.maxsize
    # 모든 집을 순회하며 나머지 집들과의 거리 구함
    for h in houses:
        cur_dist = sum([house - h for house in houses])   # 현재 집에서 모든 집까지 거리
        if dist > cur_dist:
            dist = cur_dist
            ret = h

    return ret


def solution(N, houses):
    # 최적의 안테나 설치 구역은 중앙값임
    return houses[(N - 1) // 2]


N = int(input())
houses = list(map(int, input().split()))
houses.sort()
print(solution(N, houses))