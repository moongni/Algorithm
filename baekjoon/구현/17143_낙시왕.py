from __future__ import annotations
import sys

input = sys.stdin.readline

DIRECTION = [(-1, 0), (1, 0), (0, 1), (0, -1)]

class Shark:
    def __init__(
        self,
        row: int,
        col: int,
        speed: int,
        direction: int,
        size: int
    ):
        self.row = row
        self.col = col
        self.speed = speed
        self.direction = direction
        self.size = size
    
    def __eq__(self, other: "Shark"):
        return self.size == other.size

    def __gt__(self, other: "Shark"):
        return other.size < self.size

    def __lt__(self, other: "Shark"):
        return self.size < other.size

    def __repr__(self):
        return f"<Shark pos {(self.row, self.col)} size {self.size} direction {self.direction} speed {self.speed}>"
    
    @property
    def position(self):
        return (self.row, self.col)
    
    def move(self, max_row, max_col):
        re_row_size = 2 * (max_row - 1)
        re_col_size = 2 * (max_col - 1)
        dr, dc = DIRECTION[self.direction]
        self.row, self.col = (self.row + dr * self.speed) % re_row_size, (self.col + dc * self.speed) % re_col_size
        if max_row - 1 < self.row:
            self.row = re_row_size - self.row
            self.direction = self.direction ^ 1
        elif max_col - 1 < self.col:
            self.col = re_col_size - self.col
            self.direction = 2 + ((self.direction - 2) ^ 1)
        return (self.row, self.col)
                
                
def main(row, col, sharks: list["Shark"]):
    ret = 0
    board = [[None] * (col) for _ in range((row))]
    for s in sharks:
        r, c = s.position
        board[r][c] = s
        
    for c in range(col):
        # 가장 가까운 상어를 잡음
        for r in range(row):
            if board[r][c]:
                ret += board[r][c].size
                board[r][c] = None
                break
            
        # 상어 이동
        new_board = [[None] * col for _ in range(row)]
        for pos_r in range(row):
            for pos_c in range(col):
                if board[pos_r][pos_c] is None:
                    continue
                
                shark = board[pos_r][pos_c]
                new_r, new_c = shark.move(row, col)
                
                # 상어가 곂친다면 더 큰 상어가 잡아먹음
                if new_board[new_r][new_c]:
                    if shark < new_board[new_r][new_c]:
                        continue
                new_board[new_r][new_c] = shark
        board = new_board
    return ret

R, C, M = map(int, input().split())
sharks = []
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append(Shark(r - 1, c - 1, s, d - 1, z))

if __name__ == "__main__":
    print(main(R, C, sharks))