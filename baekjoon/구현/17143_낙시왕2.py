# 이중 배열이 더 빠름 dict 선언시에 느린 듯
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
    def str_pos(self):
        return f"{self.row}:{self.col}"
    
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
    shark_map = {
        s.str_pos: s
        for s in sharks
    }
    for c in range(1, col + 1):
        # 가장 가까운 상어를 잡음
        inlines = [pos for pos in shark_map.keys() if pos.split(':')[-1] == str(c)]
        if inlines:
            shark = shark_map.pop(min(inlines, key=lambda x: int(x.split(':')[0])))
            ret += shark.size
            
        # 상어 이동
        new_shark_map = dict()
        for shark in shark_map.values():
            new_r, new_c = shark.move(row, col)
            pos_key = f"{new_r}:{new_c}"
            # 상어가 곂치면 더 큰 상어가 잡아먹음
            if new_shark_map.get(pos_key):
                if shark < new_shark_map[pos_key]:
                    continue
            new_shark_map[pos_key] = shark
        shark_map = new_shark_map
    return ret

R, C, M = map(int, input().split())
sharks = [
    Shark(*list(map(int, input().split())))
    for _ in range(M)
]

if __name__ == "__main__":
    print(main(R, C, sharks))