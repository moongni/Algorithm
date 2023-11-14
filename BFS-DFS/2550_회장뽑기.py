import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
# 각 후보자의 친구관계를 저장하는 2차원 배열
relations = [[0] * (N + 1) for _ in range(N + 1)]
while True:
    r_1, r_2 = map(int, input().split())
    if r_1 == -1 and r_2 == -1:
        break
    relations[r_1][r_2] = 1
    relations[r_2][r_1] = 1
        
def bfs(start):
    # 각 후보자의 친구관계의 깊이를 visited 배열에 저장
    visited[start] = 0
    queue = deque([[start, 0]])
    while queue:
        cur, n = queue.popleft()
        for i in range(1, N + 1):
            if relations[cur][i] == 1 and visited[i] == -1:
                visited[i] = n + 1
                queue.append([i, n + 1])

# 각 후보자의 최대 친구 관계를 사전에 저장
candidates_dict = {}
for i in range(1, N + 1):
    visited = [-1] * (N + 1)
    bfs(i)
    candidates_dict[i] = max(visited)

# 결과 출력
candidates = sorted(candidates_dict.items(), key=lambda x: (x[1], x[0]))
_,  n = candidates[0]
arr = []
for i in range(len(candidates)):
    if candidates[i][1] == n:
        arr.append(str(candidates[i][0]))
    else:
        break
    
print(n, len(arr))
print(' '.join(arr))