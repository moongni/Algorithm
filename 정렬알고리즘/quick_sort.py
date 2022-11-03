from typing import List

def partition(container: List[int], first: int, last: int) -> int:
    '''
        parameter:
        container: List[int] 정렬하기 희망하는 리스트
        first: 탐색 구간 시작지점
        last: 탐색 구간 끝나는 지점

        ------------------
        return:
            right_mark : 피봇의 위치

        pivot을 이용해 피봇 왼쪽과 오른쪽 분할
    '''
    pivot = container[first]
    left_mark = first + 1
    right_mark = last
    is_done = False

    while not is_done:
        while left_mark <= right_mark and container[left_mark] < pivot:
            left_mark += 1
        while left_mark <= right_mark and container[right_mark] >= pivot:
            right_mark -= 1
        
        if right_mark < left_mark:
            is_done = True
        else:
            container[left_mark], container[right_mark] = container[right_mark], container[left_mark]
    
    container[first], container[right_mark] = container[right_mark], container[first]

    return right_mark

def quick_sort_helper(container: List[int], start: int, end: int) -> None:
    if start < end:
        split = partition(container, start, end)

        quick_sort_helper(container, start, split - 1)
        quick_sort_helper(container, split + 1, end)

def quick_sort(container: List[int]) -> None:
    quick_sort_helper(container, 0, len(container) - 1)