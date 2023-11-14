import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
n_operators = list(map(int, input().split()))

# 사실 재귀에 가까움
# 연산량을 줄이기 위해 메모이제이션이 가능하나 5차원 배열을 사용해야함
def dfs(numbers, n_operators) -> tuple[int]:
    # base case
    if len(numbers) == 1:
        # return 최대값, 최소값
        return numbers[0], numbers[0]

    min_n = float('inf')
    max_n = float('-inf')
    for i in range(4):
        if n_operators[i] != 0:
            n_operators[i] -= 1
            if i == 0:
                cur_max, cur_min = dfs([numbers[0] + numbers[1]] + numbers[2:], n_operators)
            elif i == 1:
                cur_max, cur_min = dfs([numbers[0] - numbers[1]] + numbers[2:], n_operators)
            elif i == 2:
                cur_max, cur_min = dfs([numbers[0] * numbers[1]] + numbers[2:], n_operators)
            else:
                # c++ 나누기 연산 적용
                num = -(-numbers[0] // numbers[1]) if numbers[0] < 0 else numbers[0] // numbers[1]
                cur_max, cur_min = dfs([num] + numbers[2:], n_operators)
            n_operators[i] += 1
            min_n = min(min_n, cur_min)
            max_n = max(max_n, cur_max)
    return max_n, min_n
            
for ret in dfs(numbers, n_operators):
    print(ret)