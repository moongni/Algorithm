"""
    동적 계획법을 사용하여 이항계수 구하기
    
    이항계수 점화식 nCr = n-1Cr-1 + n-1Cr

    일반적인 재귀함수를 사용할 시 매우 많은 중복 호출이 일어남

    cache를 두어 호출 값을 저장해두어 반복호출을 줄임    
"""

cache = [[-1 for _ in range(30)] for _ in range(30)]

def bino2(n, r):
    # 기저 사례
    if r == 0 or r == n: return 1

    # cache 값 확인
    if cache[n][r] != -1:
        return cache[n][r]
    
    cache[n][r] = bino2(n-1, r-1) + bino2(n-1, r)
    
    return cache[n][r]

print(bino2(25, 12))