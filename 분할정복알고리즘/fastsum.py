"""
    n이 주어지면 1 ~ n 까지 합을 구한다.
    분할 정복 알고리즘을 사용한다.
    1 ~ n 인 n개의 조각을 n/2의 조각으로 나눈다.
    
    fastsum(n) = 1 + 2 + ... + n
              = (1 + 2 + ... + n/2) + (n/2 + 1 + n/2 + ... + n/2 + n/2)
              = (1 + 2 + ... + n/2) + n/2 * n/2 + (1 + 2 + ... + n/2)
              = fastsum(n/2) + n/2 * n/2 + fastsum(n/2)
              = 2 * fastsum(n/2) + (n/2)^2
"""
import time

def recursive_sum(n) -> int:
    if n == 1:
        return 1

    return n + recursive_sum(n - 1)

def fast_sum(n) -> int:
    # 기저조건
    if n == 1:
        return 1
    # 홀수의 경우
    elif n % 2 == 1:
        return fast_sum(n-1) + n
    # 짝수의 경우 n/2로 분할
    else:
        return 2 * fast_sum(n/2) + n/2 * n/2

# 시간 측정
start = time.time()
print(recursive_sum(2400))
end = time.time()
print(end - start)

start = time.time()
print(fast_sum(2400))
end = time.time()
print(end - start)
