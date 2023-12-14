import copy
import sys

sys.setrecursionlimit(10 ** 6)
INF = sys.maxsize

paths = []
def solution(maze):
    global paths
    
    answer = INF
    # maze에서 각 포지션을 찾음
    red_pos = [0, 0]
    red_dest = [0, 0]
    blue_pos = [0, 0]
    blue_dest = [0, 0]
    for i in range(len(maze)):
        for j in range(len(maze[0])):
            if maze[i][j] == 1:
                red_pos = [i, j]
            elif maze[i][j] == 3:
                red_dest = [i, j]
            elif maze[i][j] == 2:
                blue_pos = [i, j]
            elif maze[i][j] == 4:
                blue_dest = [i, j]
    
    # 빨간 수레가 목표까지 가는 모든 경로 구하기
    red_visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    red_visited[red_pos[0]][red_pos[1]] = True
    dfs(red_pos, red_dest, maze, red_visited, [red_pos])
    red_paths = copy.deepcopy(paths)
    
    paths = []
    
    # 파란 수레가 목표까지 가는 모든 경로 구하기
    blue_visited = [[False] * len(maze[0]) for _ in range(len(maze))]
    blue_visited[blue_pos[0]][blue_pos[1]] = True
    dfs(blue_pos, blue_dest, maze, blue_visited, [blue_pos])
    blue_paths = copy.deepcopy(paths)
    
    # 가는 경로 중 곂치는 부분이 있으면 실패
    for r_path in red_paths:
        for b_path in blue_paths:
            flag = True
            for i in range(1, max(len(r_path), len(b_path))):
                # 둘 중 하나가 먼저 도착하여 곂치는 경우
                if i >= len(r_path) or i >= len(b_path):
                    if i >= len(r_path) and r_path[-1] == b_path[i]:
                        flag = False
                        break
                    if i >= len(b_path) and b_path[-1] == r_path[i]:
                        flag = False
                        break
                else:   # 가는 도중에 곂치는 경우
                    if r_path[i] == b_path[i] \
                        or (r_path[i] == b_path[i - 1] and b_path[i] == r_path[i - 1]):
                        flag = False
                        break
            
            if flag:
                answer = min(answer, max(len(r_path), len(b_path)) - 1)
    
    return answer if answer != INF else 0

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
def dfs(pos, dest, maze, visited, path):
    global paths
    
    if pos == dest:
        return path
    
    for i in range(4):
        new_pos = [pos[0] + dy[i], pos[1] + dx[i]]
        if 0 <= new_pos[1] < len(maze[0]) and 0 <= new_pos[0] < len(maze) \
            and not visited[new_pos[0]][new_pos[1]] and maze[new_pos[0]][new_pos[1]] != 5:
            visited[new_pos[0]][new_pos[1]] = True
            new_path = dfs(new_pos, dest, maze, visited, path + [new_pos])
            if new_path is not None:
                paths.append(new_path)
            visited[new_pos[0]][new_pos[1]] = False
    return None