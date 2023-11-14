import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N, M, K, X = map(int, input().split())
cities = defaultdict(list)
for _ in range(M):
    start, end = map(int, input().split())
    cities[start].append(end)


# X에서 각 도시까지 거리를 저장, 방문하지 않은 경우 0
DISTANCES = [-1] * (N + 1) 
def bfs(start, dist):
    # start에서 각 도시가 얼마나 떨어졌는지 확인
    DISTANCES[start] = 0
    queue = deque([[start, 0]]) 
    while queue:
        city, dist_sum = queue.popleft()
        connected = cities[city]
        for c in connected:
            if DISTANCES[c] == -1:
                queue.append([c, dist_sum + 1])
                DISTANCES[c] = dist_sum + 1

    # start에서 dist만큼 떨어진 도시들 반환
    k_dist_cities = []
    for i in range(1, len(DISTANCES)):
        if DISTANCES[i] == dist:
            k_dist_cities.append(str(i))
    return k_dist_cities

k_dist_cities = bfs(X, K)
if k_dist_cities:
    print('\n'.join(k_dist_cities))
else:
    print(-1)