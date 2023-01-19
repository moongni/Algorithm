"""
    양자화

    양자화 과정은 더 넓은 범위를 갖는 값들을 작은 범위를 갖는 값들로 근사해 표현함으로써
    자료를 손실 압축하는 과정을 말한다.

    1000 이하의 자연수로 이뤄진 수열 s가 주어질 때, 가능한 오차 제곱의 합의 최소치를 구하는 프로그램을 작성하라

    ex - s: 1 2 3 4 5
            2 2 3 3 3 -> 6 
            2 2 2 3 3 -> 3

    입력
    테스트 케이스 1 <= C <= 50
    수열의 길이   1 <= n <= 100 , 사용할 숫자의 수 1 <= s <= 10
    n개의 정수    

    수열을 만들어 계산하게 되면 이전에 선택에 대한 정보가 필요하기 때문에 최적 부분 조건을 만족하지 않음
    대신 수열을 정렬해 s개의 그룹으로 묶는 문제로 변환
    최적의 양자화 계수는 정렬된 수열에서 뒤로 갈수록 증가할 것이기 때문
    n개의 수열에서
    첫 그룹 g1 = 1 ~ n - s
    둘 그룹 g2 = 1 ~ n - g1 - 1
    셋 그룹 g3 = 1 ~ n - g1 - g2 
"""

# 알고리즘 시작전에 계산해야 하는 함수
# 집합 S에 대한 정렬
# 누적합, 제곱 누적합 계산
def precalc():
    # 집합 S에 대한 정렬
    S.sort()

    # 누적합, 제곱 누적합 계산
    p_sum[0] = S[0]
    p_sq_sum[0] = S[0] * S[0]

    for i in range(1, len(S)):
        p_sum[i] = p_sum[i-1] + S[i]
        p_sq_sum[i] = p_sq_sum[i-1] + S[i] * S[i]
    
# 구간이 정해졌을 때 기준을 정하고 기준에 대한 오차 제곱을 구하는 함수
# 어떤 구간에 대해 최저 오차 제곱을 나타내는 m은 (Ai - m)^2의 미분 => m = A[i] / (end - start + 1) 평균을 의미
# 구간에 대한 평균을 구하는 것은 O(n)으로 나타낼 수 있지만, 부분합을 사용해서 O(1) 시간복잡도를 가지도록 할 수 있음

def minError(start, end):
    # 부분 합을 이용한 계산
    sum = p_sum[end]
    sq_sum = p_sq_sum[end]

    if start != 0:
        sum -= p_sum[start - 1]
        sq_sum -= p_sq_sum[start -1]

    # 반올림으로 평균구하기
    m = round(sum / (end - start + 1))

    # (Si - m)^2을 전개한 식으로 ret 도출
    ret = sq_sum - (2 * m * sum) + (m * m * (end - start + 1))

    return ret


def quantization(start, parts):
    # 기저사례 다 묶은 경우
    if len(S) == start:
        return 0
    # 더 이상 나눌 수 없는 경우
    if parts == 0: 
        return float("inf")
    # 메모이제이션
    if cache[start][parts] != -1:
        return cache[start][parts]

    cache[start][parts] = float("inf")

    for size in range(1, len(S) - start + 1):
        cache[start][parts] = min(cache[start][parts],
            minError(start, start + size - 1) + quantization(start + size, parts - 1))

    return cache[start][parts]

c = int(input())
for _ in range(c):
    n, s = map(int, input().split())
    S = list(map(int, input().split()))

    p_sum = [0] * 101
    p_sq_sum = [0] * 101
    cache = [[-1 for _ in range(11)] for _ in range(10)]

    precalc()
    print(quantization(0, s))