import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

class Dice:
    def __init__(self):
        """
          2
        4 1 3
          5
          6
        """
        self.dice = [i for i in range(1, 7)]
    
    def rotate(self, direction):
        """
        방향 + 1 -> 시계방향 90도
        방향 - 1 -> 반시계방향 90도
        방향 + 2 -> 반대방향
        0: 동
        1: 남
        2: 서
        3: 북
        """
        if direction == 0:
            rotation_ids = [3, 1, 0, 5, 4, 2]
            self.rotate_(rotation_ids)
        elif direction == 1:
            rotation_ids = [1, 5, 2, 3, 0, 4]
            self.rotate_(rotation_ids)            
        elif direction == 2:
            rotation_ids = [2, 1, 5, 0, 4, 3]
            self.rotate_(rotation_ids)
        else:
            rotation_ids = [4, 0, 2, 3, 5, 1]
            self.rotate_(rotation_ids)
            
    def rotate_(self, ids):
        new_dice = []
        for i in ids:
            new_dice.append(self.dice[i])
        self.dice = new_dice
    
    def get_bottom(self):
        return self.dice[-1]            

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
# 미리 모든 보드의 점수를 계산해두는 방법
from collections import deque

def bfs(x, y, num):
    visited[y][x] = 1
    queue = deque([[x, y]])
    connected = [[x, y]]
    cnt = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (nx >= 0 and nx < M) and (ny >= 0 and ny < N)\
                and board[ny][nx] == num and visited[ny][nx] == 0:
                    visited[ny][nx] = 1
                    queue.append([nx, ny])
                    connected.append([nx, ny])
                    cnt += 1
    for x, y in connected:
        visited[y][x] = cnt
                
visited = [[0] * M for _ in range(N)]

dice = Dice()
x, y = 0, 0
direction = 0
score = 0
for _ in range(K):
    # 방향 조정
    nx = x + dx[direction]
    ny = y + dy[direction]
    if (nx < 0 or nx >= M) or (ny < 0 or ny >= N):
        direction = (direction + 2) % 4
        nx = x + dx[direction]
        ny = y + dy[direction]
    
    num = board[ny][nx]
    if visited[ny][nx] == 0:
        bfs(nx, ny, num)
    score += num * visited[ny][nx]
        
    # 주사위 회전
    dice.rotate(direction)
    bottom = dice.get_bottom()

    # 다음 이동 방향 결정
    if bottom > num:
        direction += 1
    elif bottom < num:
        direction -= 1
    direction %= 4
    x, y = nx, ny

print(score)

# 이동별 점수를 계산하는 방식
# def dfs(x, y, num):
#     cnt = 1
#     visited[y][x] = 1
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
        
#         if (nx >= 0 and nx < M) and (ny >= 0 and ny < N) \
#             and board[ny][nx] == num and visited[ny][nx] == 0:
#                 cnt += dfs(nx, ny, num)
#     return cnt

# dice = Dice()
# x, y = 0, 0
# direction = 0
# score = 0
# for _ in range(K):
#     # 방향 조정
#     nx = x + dx[direction]
#     ny = y + dy[direction]
#     if (nx < 0 or nx >= M) or (ny < 0 or ny >= N):
#         direction = (direction + 2) % 4
#         nx = x + dx[direction]
#         ny = y + dy[direction]

#     # 현재 보드판에서 점수 얻기
#     visited = [[0] * M for _ in range(N)]
#     num = board[ny][nx]
#     score += num * dfs(nx, ny, num)

#     # 주사위 회전
#     dice.rotate(direction)
#     bottom = dice.get_bottom()

#     # 다음 이동 방향 결정
#     if bottom > num:
#         direction += 1
#     elif bottom < num:
#         direction -= 1
#     direction %= 4
#     x, y = nx, ny

# print(score)
