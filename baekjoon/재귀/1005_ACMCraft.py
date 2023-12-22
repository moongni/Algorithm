import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def get_time(node):
    conn = graph[node]
    if len(conn) == 0:
        return costs[node]
    
    if DP[node] != -1:
        return DP[node]
    
    DP[node] = 0
    candidate = []
    for c in conn:
        candidate.append(get_time(c))
    DP[node] = costs[node] + max(candidate)
    return DP[node]
    
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    costs = [0] + list(map(int, input().split()))
    graph = defaultdict(list)
    for _ in range(K):
        from_, to_ = map(int, input().split())
        graph[to_].append(from_)
    dest = int(input())
    
    DP = [-1] * (N + 1)
    print(get_time(dest))
    