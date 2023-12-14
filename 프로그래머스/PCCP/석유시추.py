from collections import deque

# 모든 열과 행에서 BFS를 한번 호출
# 호출된 BFS의 열의 누적합을 계산
def solution(land):
    depth = len(land)
    width = len(land[0])
    oil = [0] * width
    visited = [[False] * width for _ in range(depth)]
    for i in range(depth):
        for j in range(width):
            if not visited[i][j] and land[i][j] == 1:
                ret, cols = bfs(j, i, land, visited)
                for col in cols:
                    oil[col] += ret
    return max(oil)


dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def bfs(x, y, land, visited):
    oil = 0
    q = deque([(x, y)])
    cols = [x]
    visited[y][x] = True
    while q:
        x, y = q.popleft()
        oil += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < len(land[0]) and 0 <= ny < len(land) \
                and land[ny][nx] != 0 and not visited[ny][nx]:
                visited[ny][nx] = True
                cols.append(nx)
                q.append((nx, ny))
    return oil, set(cols)