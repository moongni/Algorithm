import sys
import math

input = sys.stdin.readline

N, L = map(int, input().split())

for l in range(L, 102):
    share = math.ceil(N / l)
    half = l // 2
    start = share - half
    if start < 0:
        continue
    if N == sum([i for i in range(start, start + l)]):
        break
    start += 1
    if N == sum([i for i in range(start, start + l)]):
        break
    
if l < 101:
    print(' '.join([str(i) for i in range(start, start + l)]))
else:
    print('-1')