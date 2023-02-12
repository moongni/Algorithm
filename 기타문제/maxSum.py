from typing import List

"""
    배열의 연속된 부분의 최대 부분합을 구하는 문제

    예시 [-7, 4, -3, 6, 3, -8, 3, 4] 에서 최대 부분합 [ 4, -3, 6, 3 ] : 10
"""

MIN = -99999999

# 브루트 포스
def brute_MaxSum(container: List[int]) -> int:
    """
        parameter:
            container: List[int] 숫자로 된 배열
        
        return:
            ret: int 최대 부분합
        
        시간복잡도 : O(n^2)
    """
    ret = MIN

    for i in range(len(container)):
        for j in range(i, len(container)):
            sum = 0

            for k in range(i, j + 1):
                sum += container[k]

            ret = max(ret, sum)
    
    return ret

def better_brute_MaxSum(container: List[int]) -> int:
    ret = MIN

    for i in range(len(container)):
        sum = 0
        for j in range(i, len(container)):
            sum += container[j]
            ret = max(ret, sum)

    return ret

"""
    분할 정복 알고리즘
    
    배열은 두 배열로 분할하여 각각 최대 부분합을 구한다.
    경우의 수
        1. 왼쪽 배열에 포함된 경우
        2. 오른쪽 배열에 포함된 경우
        3. 두 배열 사이에 걸쳐져 있는 경우

    기저사례
        배열의 길이가 1인 경우 요소 값 반환

"""
def divided_MaxSum(container: List[int], lo: int, hi: int) -> int:
    """
        parameter: List[int] 배열
        lo: int 구간의 시작
        hi: int 구간의 끝

        return: int 최대 부분합

        시간복잡도: O(NlogN)

    """
    # 기저사례
    if lo == hi: return container[lo]

    mid = (lo + hi) // 2

    # 두 배열 구간에 걸쳐진 부분합 구하기
    # container[i, mid] 와 container[mid + 1, j] 로 이뤄짐
    right = left = MIN
    sum = 0
    for i in range(mid, lo - 1, -1):
        sum += container[i]
        left = max(left, sum)
    
    for j in range(mid + 1, hi + 1):
        sum += container[j]
        right = max(right, sum)
    
    # 분할한 배열 중 가장 높은 부분합 구하기
    single = max(divided_MaxSum(container, lo, mid),
                    divided_MaxSum(container, mid + 1, hi))
    
    return max(left + right, single)

"""
    동적계획법

    배열의 container[i]를 오른쪽 끝에 포함한 최대 부분합을 구하는 함수 maxAt(i)를 정의했을 때
    최대 부분합은 
    container[i - 1] 에 container[i]를 포함한 모양 또는 container[i] 임
    점화식으로 변경하면
    maxAt(i) = max(0, maxAt(i - 1)) + container[i]

"""
def dynamic_MaxSum(container: List[int]) -> int:
    ret = MIN
    psum = 0

    for i in range(len(container)):
        psum = max(psum, 0) + container[i]
        ret = max(psum, ret)

    return ret

if __name__ == "__main__":
    print(brute_MaxSum([-7, 4, -3, 6, 3, -8, 3, 4]))
    print(better_brute_MaxSum([-7, 4, -3, 6, 3, -8, 3, 4]))
    print(divided_MaxSum([-7, 4, -3, 6, 3, -8, 3, 4], 0, len([-7, 4, -3, 6, 3, -8, 3, 4]) - 1))
    print(dynamic_MaxSum([-7, 4, -3, 6, 3, -8, 3, 4]))
