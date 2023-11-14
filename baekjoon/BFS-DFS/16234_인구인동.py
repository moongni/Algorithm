import sys
from collections import deque

input = sys.stdin.readline

N, L, R = map(int, input().split())
countries = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs(x, y):
    visited[y][x] = 1
    queue = deque([[x, y]])
    associations = [[x, y]]
    # 방문한 나라의 인구 수 합과 나라의 수를 저장할 변수
    total_population = countries[y][x]
    cnt_country = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (nx < 0 or nx >= N) or (ny < 0 or ny >= N) or visited[ny][nx] == 1:
                continue
            
            diff = abs(countries[y][x] - countries[ny][nx])
            if diff >= L and diff <= R:
                visited[ny][nx] = 1
                queue.append([nx, ny])
                associations.append([nx, ny])
                total_population += countries[ny][nx]
                cnt_country += 1
                
    if len(associations) > 1:
        mean = total_population // cnt_country
        for x, y in associations:
            countries[y][x] = mean        
        return True            
    return False


days = 0
while True:
    visited = [[0] * N for _ in range(N)]
    is_move = False
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                is_move = bfs(j, i) or is_move

    if not is_move:
        break

    days += 1

print(days)