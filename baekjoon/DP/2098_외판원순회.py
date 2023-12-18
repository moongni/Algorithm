import sys

input = sys.stdin.readline
INF = sys.maxsize

N = int(input())
cost = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (1 << N) for _ in range(N)]
END = (1 << N) - 1

def TSP(now, visited):
    # 모든 노드 방문 bit: 1*N
    if visited == END:
        # 순환이 가능하다면 최소 비용 반환
        if cost[now][0] > 0:
            return cost[now][0]
        return INF

    if dp[now][visited] != 0:
        return dp[now][visited]
    
    dp[now][visited] = INF
    for i in range(N):
        # 연결되지 않은 노드
        if cost[now][i] == 0: continue
        # 이미 방문 노드
        if visited & (1 << i): continue
        min_cost = TSP(i, visited | (1 << i))
        dp[now][visited] = min(dp[now][visited], cost[now][i] + min_cost)
    return dp[now][visited]

print(TSP(0, 1))