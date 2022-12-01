"""
    보드 덮기 게임
    H x W 크기의 게임판은 검은 칸과 흰 칸으로 구성되어있다. 이중 모든 흰 칸을 세 칸짜리 L자 모양의 블록으로 덮고 싶다.
    블록은 자유롭게 회전해서 놓을 수 있지만 곂치거나 검은 칸을 덮거나 게임판 밖으로 나갈 수 없다.
    보드를 입력하면 덮을 수 있는 경우의 수 출력

    풀이 생각
    왼쪽 위에서부터 검은칸 패스 흰칸일 때 L_BLOCK 중 하나로 덮이면 보드변경 후 재귀 후 보드 취소
"""
# 내가 생각한 코드

# L_BLOCK 이 가능한 경우의 수 역ㄱ, 역ㄴ, ㄴ, ㄱ
L_BLOCK = [
    [(0, 1), (1, 0)], 
    [(1, 0), (1, -1)], 
    [(1, 0), (1, 1)], 
    [(0, 1), (1, 1)]
]

# L자 블록 중 하나로 덮일 수 있는 지 판단
def is_boardCover(h, w, l_case, board):
    flag = True

    for l_h, l_w in l_case:
        # 보드를 벗어나는지 확인
        if (h + l_h < 0 or h + l_h >= len(board)) or \
            (w + l_w < 0 or w + l_w >= len(board[0])):
            return False

        # l_case가 가능한지 확인
        if not(board[h + l_h][w + l_w] == "."):
            flag = False

    return flag

# L자 블록으로 덮이는 경우의 수 출력
def boardcover(board):
    ret = 0

    h = w = 0

    flag = False
    # 가장 왼쪽 위 흰 칸 찾기
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == ".":
                h = row
                w = col
                flag = True
                break
        if flag:
            break

    if not(flag):
        return 1

    # L_BLOCK이 가능한지 확인
    for l_case in L_BLOCK:
        if is_boardCover(h, w, l_case, board):
            board[h][w] = "#"
            for l_h, l_w in l_case:
                board[h + l_h][w + l_w] = "#"
            
            ret += boardcover(board)
            
            board[h][w] = "."
            for l_h, l_w in l_case:
                board[h + l_h][w + l_w] = "."
        
    return ret

BOARD = [["#", ".", ".", ".", ".", ".", "#"],
         ["#", ".", ".", ".", ".", ".", "#"],
         ["#", "#", ".", ".", ".", "#", "#"]]
BOARD2 = [["#", ".", ".", ".", ".", ".", "#"],
          ["#", ".", ".", ".", ".", ".", "#"],
          ["#", "#", ".", ".", "#", "#", "#"]]
BOARD3 = [
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", ".", ".", ".", ".", ".", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#"]]

print(boardcover(BOARD))
print(boardcover(BOARD2))
print(boardcover(BOARD3))