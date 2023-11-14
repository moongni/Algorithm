import sys
input = sys.stdin.readline


def solution(reservations: list):
    reservations.sort(key=lambda x: (x[1], x[0]))   # 끝나는 시간을 기준으로 정렬
    cnt = 0
    end = 0
    for r in reservations:
        if end <= r[0]:
            cnt += 1
            end = r[1]
    return cnt

    
N = int(input())
reservations = [list(map(int, input().split())) for _ in range(N)]
print(solution(reservations))