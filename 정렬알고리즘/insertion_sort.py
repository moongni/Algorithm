from typing import List

def insertion_sert(container: List[int]) -> None:
    '''
        parameter:
        container: List[int] 정렬하기 희망하는 리스트

        ------------------

        return:
            sortedList: List[int] 정렬된 리스트

        ------------------

        리스트에서 현재 인덱스의 앞 인덱스와 비교해 더 작으면 스왑함

    '''
    if len(container) == 0:
        return []
        
    for i in range(1, len(container)):
        j = i
        
        while j > 0 and container[j - 1] > container[j]:
            container[j - 1], container[j] = container[j], container[j - 1]
            j -= 1


def shell_sort(container: List[int]) -> None:
    length = len(container)
    gap = length // 2

    while gap > 0:
        if gap % 2 == 0:
            gap += 1

        for start in range(gap):
            # insertion sort
            for i in range(start + gap, length, gap):
                j = i

                while j > start and container[j - gap] > container[j]:
                    container[j - gap], container[j] = container[j], container[j - gap]
                    j -= gap

        gap //= 2