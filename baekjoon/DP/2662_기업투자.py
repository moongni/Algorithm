import sys

input = sys.stdin.readline

N, M = map(int, input().split())
portfolios = [[0] * (M + 1)]
for _ in range(N):
    portfolio = list(map(int, input().split()))
    portfolios.append(portfolio)

dp = [[0] * (N + 1) for _ in range(M + 1)]
dp2 = [[0] * (N + 1) for _ in range(M + 1)]
for m in range(1, M + 1):
    for n in range(1, N + 1):  
        # 현재 m 기업에 i만큼 투자했을 경우
        for i in range(n, -1, -1):
            # m 제품을 투자한 경우 + 이전 m - 1번 까지의 제품을 활용한 최대 수익
            profit = portfolios[i][m] + dp[m-1][n - i]
            if dp[m][n] < profit:
                dp[m][n] = profit
                dp2[m][n] = i

print(dp[-1][-1])

n = N
pf = []
for i in range(M, 0, -1):
    curr = dp2[i][n]
    pf.append(str(curr))
    n -= curr
    
print(' '.join(reversed(pf)))