import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n = int(input())

cache = [-1] * (n + 1)
def top_down(n):
    if n == 1:
        return 1
    if n == 2:
        return 3

    if cache[n] != -1:
        return cache[n]

    cache[n] = top_down(n - 1) + (2 * top_down(n - 2))
    return cache[n]

def bottom_up(n):
    prev, curr = 1, 3
    if n == 1:
        return prev
    if n == 2:
        return curr
    
    for _ in range(2, n):
        prev, curr = curr, curr + 2 * prev
    
    return curr

print(top_down(n) % 10_007)
print(bottom_up(n))