import sys
sys.setrecursionlimit(10**6)

MOD = 1_000_000_007
DP = [0, 1, 3, 10, 23, 62, 170] + [0] * 100_000

def solution(n):
    for i in range(7, n + 1):
        DP[i] += DP[i - 1]
        DP[i] += DP[i - 2] * 2
        DP[i] += DP[i - 3] * 6
        DP[i] += DP[i - 4]
        DP[i] -= DP[i - 6]
    return DP[n] % MOD