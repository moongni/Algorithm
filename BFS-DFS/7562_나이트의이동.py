import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

MOVES = [
    [-2, 1], [-1, 2], [1, 2], [2, 1],
    [-2, -1], [-1, -2], [1, -2], [2, -1]
]
def bfs(pos):
    queue = deque([pos])  # [row, col, move count]
    while queue:
        row, col = queue.popleft()
        if row == dest_pos[0] and col == dest_pos[1]:
            return maps[row][col]
        
        for move in MOVES:
            new_row, new_col = row + move[0], col + move[1]
            if (new_row < 0 or new_row >= I) or (new_col < 0 or  new_col >= I):
                continue 
            if maps[new_row][new_col] == -1:
                maps[new_row][new_col] = maps[row][col] + 1
                queue.append([new_row, new_col])

for _ in range(T):
    I = int(input())
    maps = [[-1] * I for _ in range(I)]
    cur_pos = list(map(int, input().split()))
    dest_pos = list(map(int, input().split()))
    maps[cur_pos[0]][cur_pos[1]] = 0
    print(bfs(cur_pos))