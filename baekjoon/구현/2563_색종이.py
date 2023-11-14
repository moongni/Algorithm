import sys

input = sys.stdin.readline

N = int(input())
papers = [list(map(int, input().split())) for _ in range(N)]

def solution(papers):
    ret = 0
    board = [[0 for _ in range(100)] for _ in range(100)]
    for s_col, s_row in papers:
        for col in range(s_col, s_col+10):
            for row in range(s_row, s_row+10):
                if board[row][col] == 0:
                    board[row][col] = 1
                    ret += 1
    return ret

print(solution(papers))

checked = set()
for paper in papers:
    checked = checked.union(
    set([(i, j) for i in range(paper[0], paper[0] + 10) \
                for j in range(paper[1], paper[1] + 10)]))
print(len(checked))