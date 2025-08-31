# 시간초과
import sys

input = sys.stdin.readline

def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]

def union(a, b):
    a, b = find(a), find(b)
    if a != b:
        parents[b] = a
        n_friends[a] += n_friends[b]


C = int(input())
for _ in range(C):
    N = int(input())
    idx = 0
    index_map = dict()
    parents = [i for i in range(2*N)]
    n_friends = [1 for _ in range(2*N)]
    for _ in range(N):
        f1, f2 = input().split()
        if f1 not in index_map:
            index_map[f1] = idx
            idx += 1
        if f2 not in index_map:
            index_map[f2] = idx
            idx += 1
        
        f1_id = index_map[f1]
        f2_id = index_map[f2]
        union(f1_id, f2_id)
        print(n_friends[find(f1_id)])