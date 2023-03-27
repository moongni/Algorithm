import math

def solution(arr):
    # 피연산자의 수
    operands_count = math.ceil(len(arr) / 2)
    # i번째 피연산자에서 j번째 피연산자의 최대값을 저장
    max_dp = [[float('-inf')] * operands_count for _ in range(operands_count)]
    # i번째 피연산자에서 j번째 피연산자의 최소값을 저장
    min_dp = [[float('inf')] * operands_count for _ in range(operands_count)]

    # 각 피연산자들 위치에 max, min값 저장
    for i in range(operands_count):
        max_dp[i][i] = min_dp[i][i] = int(arr[i*2])

    # 연산자가 n - 1개 이므로 n-1번 순회
    for cnt in range(1, operands_count):
        print('cnt', cnt)
        # 0 ~ n - 2
        for i in range(operands_count - cnt):
            #  n
            j = i + cnt
            print('i:', i, 'j:',j)
            for k in range(i, j):
                print('k:', k)
                if arr[k * 2 + 1] == '+':
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k+1][j])
                else:
                    max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k+1][j])
                    min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k+1][j])
    
    return max_dp[0][operands_count - 1]

solution(["1", "-", "3", "+", "5", "-", "8"])