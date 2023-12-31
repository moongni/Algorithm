import sys

input = sys.stdin.readline

T = int(input())

def fibbo(n):
    if n == 0:
        return [1, 0]
    if n == 1:
        return [0, 1]
    if DP[n][0] != -1 or DP[n][1] != -1:
        return DP[n]
    
    DP[n] = [0, 0]
    f1 = fibbo(n - 1)
    f2 = fibbo(n - 2)
    DP[n][0] = f1[0] + f2[0]
    DP[n][1] = f1[1] + f2[1]
    return DP[n]
    

for _ in range(T):
    N = int(input())
    DP = [[-1, -1] for _ in range(N + 1)]
    answer = fibbo(N)
    print(' '.join(map(str, answer)))