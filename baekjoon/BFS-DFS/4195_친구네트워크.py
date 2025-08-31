# BFS 시간초과

import sys
from collections import defaultdict

input = sys.stdin.readline

def count_friends(start, network):
    ret = 0
    stack = [start]
    visited = set()
    while stack:
        name = stack.pop()
        for linked in network[name]:
            if linked not in visited:
                ret += 1
                visited.add(linked)
                stack.append(linked)
    return ret


C = int(input())
for _ in range(C):
    N = int(input())
    network = defaultdict(set)
    for _ in range(N):
        f1, f2 = input().split()
        network[f1].add(f2)
        network[f2].add(f1)
        print(count_friends(f1, network))