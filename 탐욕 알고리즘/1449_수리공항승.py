def solution(length, points):
    points.sort()
    
    start = points[0]
    cnt = 0
    for point in points:
        # 시작점부터 끝까지 거리
        diff = point - start
        if diff >= length:
            start = point
            cnt += 1
    
    return cnt + 1

N, L = map(int, input().split())
points = list(map(int, input().split()))
print(solution(L, points))