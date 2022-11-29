from typing import List

def binary_search(container: List[int], item: int) -> int:
    """
        필수 조건: container는 오름차순으로 정렬된 리스트
        결과 container[i - 1] < item <= container[i] 인 i를 반환한다.

    """

    n = len(container)
    hi = n; lo = -1

    while lo + 1 < hi:
        mid = (lo + hi) // 2

        if container[mid] < item:
            lo = mid
        else:
            hi = mid
        
    return hi