"""
    보글 게임 5x5 의 알파벳 격자에서 상하좌우/대각선 인접한 칸의 글자를 이어서 단어를 찾아낸다.

    
"""
from typing import List

BOARD: List[List[str]] = \
[["U", "R", "L", "P", "M"],
 ["X", "P", "R", "E", "T"],
 ["G", "I", "A", "E", "T"],
 ["X", "T", "N", "Z", "Y"],
 ["X", "O", "Q", "R", "S"]]

def boggle(x, y, word: str) -> bool:
    # 보드 범위 밖으로 나간경우
    if (x < 0 or y < 0) or (x >= len(BOARD) or y >= len(BOARD[0])):
        return False

    # 보드의 글자가 다른경우    
    if (BOARD[x][y] != word[0]):
        return False
    elif len(word) == 1:
        return True

    for i in range(-1, 2):
        for j in range(-1, 2):
            if boggle(x + i, y + j, word[1:]):
                return True

    return False

print(boggle(1, 1, "PRETTY"))
print(boggle(2, 0, "GIRL"))
print(boggle(1, 2, "REPEAT"))