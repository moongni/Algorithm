import sys

input = sys.stdin.readline

N, M = map(int, input().split())
metrix = [list(map(int, input().split())) for _ in range(N)]

TETROMINO = [
    # 윗줄이 4칸
    [(0, 3), (0, 2), (0, 1)],   # ----
    # 3칸    
    [(0, 2), (1, 2), (0, 1)],   # --ㅜ
    [(0, 2), (1, 1), (0, 1)],   # -ㅜ-
    [(0, 2), (1, 0), (0, 1)],   # ㅜ--
    [(0, 2), (-1, 2), (0, 1)],  # --ㅗ
    [(0, 2), (-1, 1), (0, 1)],  # -ㅗ-
    [(0, 2), (-1, 0), (0, 1)],  # ㅗ--
    [(1, 2), (1, 1), (0, 1)],
    [(-1, 2), (-1, 1), (0, 1)],
    # 2칸
    [(0, 1), (1, 1), (1, 0)],   # []
    [(0, 1), (1, 0), (2, 0)],   # ㅜ-
    [(1, 1), (1, 0), (2, 0)],   # ㅏ
    [(2, 1), (1, 0), (2, 0)],   # L
    [(0, 1), (1, 1), (2, 1)],   # -ㅜ
    [(-1, 1), (0, 1), (1, 1)],  # ㅓ
    [(-2, 1), (-1, 1), (0, 1)], # -ㅣ
    [(2, 1), (1, 1), (1, 0)],
    [(2, -1), (1, -1), (1, 0)],
    
    # 1칸
    [(3, 0), (2, 0), (1, 0)]    # |
]

max_num = max(map(max, metrix))

def get_max(metrix):
    ret = 0
    # 메트릭스 순회
    for row in range(N):
        for col in range(M):
            # 가능한 테트로미노 조합 순회 19개
            for tet in TETROMINO:
                cur_max = metrix[row][col]
                for i, (row_idx, col_idx) in enumerate(tet):    # 3개
                    if cur_max + (3 - i) * max_num < ret:
                        break
                    new_row = row + row_idx
                    new_col = col + col_idx
                    if new_row < 0 or new_row >= N \
                        or new_col < 0 or new_col >= M:
                        break
                    cur_max += metrix[new_row][new_col]
                ret = max(ret, cur_max)
    return ret

print(get_max(metrix))