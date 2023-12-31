import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
graph = [input().rstrip() for _ in range(N)]

def BFS(n):
    ret = 0
    queue = deque([(n, 0)])
    visited[n] = True
    while queue:
        n, n_friends = queue.popleft()
        if n_friends >= 2:
            continue
        for i, conn in enumerate(graph[n]):
            if conn == 'Y' and not visited[i]:
                queue.append((i, n_friends + 1))
                visited[i] = True
                ret += 1
    return ret
    
answer = 0            
for n in range(N):
    visited = [False] * N
    answer = max(answer, BFS(n))
print(answer)