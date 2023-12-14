import heapq
import sys

input = sys.stdin.readline
INF = sys.maxsize

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dijkstra(n):
    maps = [list(map(int, input().split())) for _ in range(N)]
    
    H = [(maps[0][0], 0, 0)]    # distance, x, y
    while H:
        dist, x, y = heapq.heappop(H)
        if y == n - 1 and x == n - 1:
            ret = dist
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0 <= nx < n) and (0 <= ny < n) and maps[ny][nx] != -1:
                heapq.heappush(H, (dist + maps[ny][nx], nx, ny))
                maps[ny][nx] = -1
    return ret    

        

idx = 0
while True:    
    idx += 1
    N = int(input())
    if N == 0:
        break
    print(f"Problem {idx}: {dijkstra(N)}")