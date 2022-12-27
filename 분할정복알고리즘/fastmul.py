"""
    카라츠바 빠른 곱셈
    Karatsuba
    
    수만 자리의 정수를 곱할시에 사용
    두 수를 각각 절반으로 쪼갬
    a, b가 256 자리 수의 경우 128 자리로 나눔 
    a = a1 x 10^128 + a0
    b = b1 x 10^128 + b0

    a x b = (a1 x 10^128 + a0) x (b1 x 10^128 + b0)
          = a1 x b1 x 10^256 + (a1 x b0 + b1 x a0) x 10^128 + a0 x b0
    
    위 식처럼 분할하여 4번을 곱한다. 10의 거듭제곱은 시프트 연산을 통해 구현할시
    시프트 연산 시간복잡도 O(n)
    전체 수행 시간복잡도 O(n^2)

    카라츠바의 경우 a x b 를 세번의 곱으로 변환
    (a0 + a1) x (b0 + b1) = a0 x b0 + (a1 x b0 + a0 x b1) + a1 x b1
                            _______    _________________    _______
    z0 = a0 x b0 ------ 1
    z2 = a1 x b1 ------ 1
    z1 = a1 x b0 + a0 x b1 = (a0 + a1) x (b0 + b1) - z0 - z2 ------ 1
    
    그 후 세 결과를 조합해 원래 두수의 답을 구한다.

    미해결
"""

# O(n^2) 곱셈 알고리즘
def multiply(a, b):
    c = [0] * (len(a) * len(b) + 1)

    for i in range(len(a)):
        for j in range(len(b)):
            c[i + j] += a[i] * b[j]
    
    return c

# a += b * 10^k
def addTo(a, b, k):
    if len(a) < len(b) + k:
        a.extend([0] * (len(b) + k - len(a)))

    for i in range(len(b)):
        a[i + k] += b[i]

def subFrom(a, b):
    if len(a) < len(b):
        a.extend([0] * (len(b) - len(a)))    
    
    for i in range(len(b)):
        a[i] -= b[i]

def karatsuba(a, b):
    an, bn = len(a), len(b)

    # b의 자리수가 더 큰 경우
    if (an < bn): return karatsuba(b, a)

    # 기저사례 a 또는 b가 빈 경우
    if an == 0 or bn == 0: return 0
    if an <= 10: return multiply(a, b)

    half = an // 2
    a0 = a[:half]
    a1 = a[half:]
    b0 = b[:min(half, len(b))]
    b1 = b[min(half, len(b)):]
    print(a0, a1)
    print(b0, b1)
    # z2 = a1 x b1
    z2 = karatsuba(a1, b1)
    # z0 = a0 x b0
    z0 = karatsuba(a0, b0)
    # a0 = a0 + a1 , b0 = b0 + b1
    a0 = addTo(a0, a1, 0)
    b0 = addTo(b0, b1, 0)

    # z1 = (a0 + a1) x (b0 + b1)
    z1 = karatsuba(a0, b0)
    
    subFrom(z1, z0)
    subFrom(z1, z2)

    ret = []
    addTo(ret, z0, 0)
    addTo(ret, z1, half)
    addTo(ret, z2, half + half)

    return ret

print(karatsuba([2] * 256, [1] * 256))