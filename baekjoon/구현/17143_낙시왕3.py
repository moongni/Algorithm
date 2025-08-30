# 시간초과
from __future__ import annotations
import sys

input = sys.stdin.readline


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
        return self.row, self.col
    
    def move(self, max_row, max_col):
        move_range = self.speed
        while 0 < move_range:
            if self.direction == 1:
                diff = self.row - 1
                if diff < move_range:
                    move_range -= diff
                    self.direction = 2
                    self.row -= diff
                else:
                    self.row -= move_range
                    move_range = 0
            elif self.direction == 2:
                diff = max_row - self.row
                if diff < move_range:
                    move_range -= diff
                    self.direction = 1
                    self.row += diff
                else:
                    self.row += move_range
                    move_range = 0
            elif self.direction == 3:
                diff = max_col - self.col
                if diff < move_range:
                    move_range -= diff
                    self.direction = 4
                    self.col += diff
                else:
                    self.col += move_range
                    move_range = 0
            elif self.direction == 4:
                diff = self.col - 1
                if diff < move_range:
                    move_range -= diff
                    self.direction = 3
                    self.col -= diff
                else:
                    self.col -= move_range
                    move_range = 0
        return (self.row, self.col)
                
                
def main(row, col, sharks: list["Shark"]):
    ret = 0
    for c in range(1, col + 1):
        # 가장 가까운 상어를 잡음
        inlines = [i for i, s in enumerate(sharks) if s.col == c]
        if inlines:
            ret += sharks.pop(min(inlines)).size
        
        # 상어 이동
        new_sharks = []
        for shark in sharks:
            new_r, new_c = shark.move(row, col)
            for i in range(len(new_sharks)):
                if (new_r, new_c) == new_sharks[i].position:
                    if new_sharks[i] < shark:
                        new_sharks[i] = shark
                        continue
            new_sharks.append(shark)
            
    return ret

R, C, M = map(int, input().split())
sharks = [
    Shark(*list(map(int, input().split())))
    for _ in range(M)
]

if __name__ == "__main__":
    print(main(R, C, sharks))