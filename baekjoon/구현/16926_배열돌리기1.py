import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
arr = [list(input().split()) for _ in range(N)]

def rotate_board(arr, R):
    n_rotation = min(N, M) // 2
    new_arr = [[0 for _ in range(M)] for _ in range(N)]
    for pos in range(n_rotation):  # 회전시킬 위치
        # 로테이션
        r = R % ((N-2*pos) * 2 + max(0, (M-2*pos-2)) * 2)   # 한바퀴를 안도는 내에서 회전 수
        cur_arr = arr[pos][pos:M-pos]            # 위 row
        for row in range(pos+1, N-pos-1):        # 우측 col    
            cur_arr.append(arr[row][M-pos-1])
        cur_arr += arr[N-pos-1][pos:M-pos][::-1] # 아래 row
        for row in range(N-pos-2, pos, -1):      # 왼쪽 col
            cur_arr.append(arr[row][pos])
        cur_arr = cur_arr[r:] + cur_arr[:r]
        
        # 배열로 복구
        for row in range(pos+1, N-pos-1):
            new_arr[row][pos] = cur_arr.pop()
        for col in range(pos, M-pos):
            new_arr[N-pos-1][col] = cur_arr.pop()
        for row in range(N-pos-2, pos, -1):
            new_arr[row][M-pos-1] = cur_arr.pop()
        for col in range(M-pos-1, pos-1, -1):
            new_arr[pos][col] = cur_arr.pop()
    return new_arr
        
arr = rotate_board(arr, R)    
for row in arr:
    print(' '.join(row))