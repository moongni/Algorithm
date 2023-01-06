"""
    합친 LIS
    두 개의 정수 수열 A와 B에서 각각 길이 0 이상의 증가 부분 수열을 얻은 뒤 이들을 크기 순서대로 합친 것을 합친 부분 증가 수열이라고 부르기로 한다.
    ex - '1 3 4 7 9'는 '1 9 4'와 '3 4 7'의 합친 LIS이다.

    입력
    첫 줄 테스트 케이스 수 C(1 <= C <= 50)
    각 첫 줄 A, B의 길이 n, m
    다음 줄 n개의 정수로 이뤄진 A원소
    다음 줄 m개의 정수로 이뤄진 B원소

    출력
    각 테스트 케이스마다 한줄에 JLIS의 길이를 출력한다.
"""

def jlis(A, B, indexA=-1, indexB=-1):
    # 메모이제이션
    if cache[indexA+1][indexB+1] != -1:
        return cache[indexA+1][indexB+1]
    
    # A[indexA] B[indexB]가 이미 존재함으로 항상 2개 이상
    cache[indexA+1][indexB+1] = 2

    a = A[indexA]
    b = B[indexB]
    
    if indexA == -1:
        a = float("-inf")
    if indexB == -1:
        b = float("-inf")

    maxElement = max(a, b)

    for nextA in range(indexA + 1, len(A)):
        if maxElement < A[nextA]:
            cache[indexA+1][indexB+1] = \
                max(cache[indexA+1][indexB+1], jlis(A, B, nextA, indexB) + 1)
            
    for nextB in range(indexB + 1, len(B)):
        if maxElement < B[nextB]:
            cache[indexA+1][indexB+1] = \
                max(cache[indexA+1][indexB+1], jlis(A, B, indexA, nextB) + 1)
    
    return cache[indexA+1][indexB+1]

# 테스트 케이스
testcase = int(input())

for case in range(testcase):
    n, m = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    cache = [[-1 for _ in range(51)] for _ in range(51)]
    print(jlis(A, B) - 2)