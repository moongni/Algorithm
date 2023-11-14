import sys
import heapq

input = sys.stdin.readline

def solution(classes):
    # 가장 빨리 시작하는 강의 순으로 정렬
    classes.sort()
    # 가장 빨리 비는 강의실을 유지하기 위해 우선순위 큐로 구현
    rooms = []
    heapq.heappush(rooms, 0)
    for c in classes:
        # 빈 강의실이 존재하는 경우
        if rooms[0] <= c[0]:
            heapq.heappop(rooms)
            heapq.heappush(rooms, c[1])
        # 새로운 강의실 할당
        else:
            heapq.heappush(rooms, c[1])

    return len(rooms)
    
N = int(input())
classes = [list(map(int, input().split())) for _ in range(N)]
print(solution(classes))