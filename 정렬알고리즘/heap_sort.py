from typing import List

def heapify(container: List[int], idx: int, length: int) -> None:
    """
        parameter:
            container: List[int] 정렬할 배열
            largest: int 부모 인덱스
            length: int 배열 길이
        -------------------

        return: None
    """
    largest = idx
    left = 2 * idx + 1
    right = 2 * idx + 2

    if left < length and container[idx] < container[left]:
        largest = left
    
    if right < length and container[largest] < container[right]:
        largest = right
    
    if largest != idx:
        container[largest], container[idx] = container[idx], container[largest]
        heapify(container, largest, length)
    
def heap_sort(container: List[int]) -> None:
    length = len(container)

    for i in range(length // 2 - 1, -1 , -1):
        heapify(container, i, length)
    
    for i in range(length - 1, 0, -1):
        container[i], container[0] = container[0], container[i]
        heapify(container, 0, i)