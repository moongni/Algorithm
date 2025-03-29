import sys

input = sys.stdin.readline

N = int(input())

def solution(n: int) -> int:
    """
    숫자를 입력받아 소수의 연속합으로 표현가능한 조합의 수를 반환
    """
    ret = 0
    
    # Step 1: 에라토스테네스의 체를 통해 n보다 작거나 같은 소수를 계산
    primes = get_primes(n)
    
    # Step 2: 구간합을 진행하며 구간합으로 n이 만들어지는 경우의 수를 체크
    # 만약 sum이 n보다 커진다면 조기 종료
    for i in range(len(primes)):
        sum = 0
        for j in range(i, len(primes)):
            sum += primes[j]
            if n <= sum:
                break
        if n == sum:
            ret += 1
                
    # Step 3: 가능한 경우의 수 반환
    return ret


def get_primes(n: int) -> list[int]:
    """에라토스테네스의 체를 사용해 n보다 작은 소수 배열 반환"""
    primes = [False, False] + [True] * (n-1)
    for i in range(2, n + 1):
        if primes[i]:
            for j in range(2 * i, n + 1, i):
                primes[j] = False
    return [i for i in range(len(primes)) if primes[i]]


print(solution(N))

if __name__ == "__main__":
    print(get_primes(41))