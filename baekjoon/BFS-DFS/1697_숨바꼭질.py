import sys
from collections import deque

input = sys.stdin.readline
N, K = map(int, input().split())

def bfs(n, k):
    queue = deque([[n, 0]])
    visited[n] = 1
    while queue:
        pos, step = queue.popleft()
        if pos == k:
            return step
        
        for new_pos in [pos - 1, pos + 1, 2 * pos]:
            if new_pos < 0 or new_pos > 100_000 or visited[new_pos] == 1:
                continue
            visited[new_pos] = 1
            queue.append([new_pos, step + 1])
                            
visited = [-1] * 100_001
print(bfs(N, K))


## 탐욕법
def greedy(n, k):
    if n >= k:
        return n - k
    if n + 1 == k:
        return 1

    if k % 2:    # k가 홀수
        return min(greedy(n, k - 1), greedy(n, k + 1)) + 1
    # k가 짝수
    return min(k - n, greedy(n, k // 2) + 1)

print(greedy(N, K))
        