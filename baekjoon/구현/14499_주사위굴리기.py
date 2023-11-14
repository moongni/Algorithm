import sys
import copy

input = sys.stdin.readline


class Dice:
    def __init__(self,):
        """
              1
            3 0 2
              4
              5
        """
        self.dice = [0] * 6

    def rotate(self, direction: int):
        """
            1: 동쪽
            2: 서쪽
            3: 북쪽
            4: 남쪽
        """
        if direction == 1:
            rotation_ids = [3, 1, 0, 5, 4, 2]
            self.dice = self.rotate_(rotation_ids)
        elif direction == 2:
            rotation_ids = [2, 1, 5, 0, 4, 3]
            self.dice = self.rotate_(rotation_ids)
        elif direction == 3:
            rotation_ids = [4, 0, 2, 3, 5, 1]
            self.dice = self.rotate_(rotation_ids)
        else:
            rotation_ids = [1, 5, 2, 3, 0, 4]
            self.dice = self.rotate_(rotation_ids)

    def rotate_(self, rotation_ids):
        new_dice = copy.copy(self.dice)
        for idx, new_idx in enumerate(rotation_ids):
            new_dice[idx] = self.dice[new_idx]
        return new_dice

    def get_top(self):
        return self.dice[0]

    def get_bottom(self):
        return self.dice[-1]

    def set_bottom(self, num):
        self.dice[-1] = num

#     def __str__(self):
#         return f"""\
#   {self.dice[1]}
# {self.dice[3]} {self.dice[0]} {self.dice[2]}
#   {self.dice[4]}
#   {self.dice[5]}"""


N, M, y, x, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
commands = list(map(int, input().split()))

dice = Dice()
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for command in commands:
    nx = x + dx[command - 1]
    ny = y + dy[command - 1]
    # 게임판을 벗어난 경우
    if (nx < 0 or nx >= M) or (ny < 0 or ny >= N):
        continue

    dice.rotate(command)
    if board[ny][nx] == 0:
        board[ny][nx] = dice.get_bottom()
    else:
        dice.set_bottom(board[ny][nx])
        board[ny][nx] = 0
    x, y = nx, ny
    print(dice.get_top())
