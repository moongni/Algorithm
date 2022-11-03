from typing import List

def selection_sort(container: List[int]) -> None:
    '''
        parameter:
        container: List[int] 정렬하기 희망하는 리스트

        ------------------

        리스트에서 가장 작은 수를 찾아 앞에 삽입하는 정렬

        3, 5, 6, 1, 2

        1st : 1, 3, 5, 6, 2
        2nd : 1, 2, 3, 5, 6
    '''
    if len(container) == 0:
        return []
        
    for i in range(len(container)):
        minIndex = i

        for j in range(i+1, len(container)):
            if container[minIndex] > container[j]:
                minIndex = j
        
        container[i], container[minIndex] = container[minIndex], container[i]
    
    return container
