def eratosthenes(num: int = 3000):
    a = [False, False] + [True] * (num - 1)
    primes = []
    for i in range(2, num+1):
        if a[i]:
            primes.append(i)
        for j in range(2*i, num+1, i):
            a[j] = False
    return set(primes)

def solution(nums):
    answer = 0
    eratos = eratosthenes()
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] in eratos:
                    answer += 1
    return answer