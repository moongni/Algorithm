from typing import List

def bubble_sort(container: List[int]) -> None:
    '''
        parameter:
        container: List[int] 정렬하기 희망하는 리스트

        ------------------

        return:
            sortedList: List[int] 정렬된 리스트

        ------------------

        리스트를 뒤에 것과 비교해 더 크면 바꾸며 가장 큰 수를 뒤로 보내는 알고리즘
        정렬이 완료되면 중간에 반환 가능
    '''
    # 입력 리스트 길이가 0
    if len(container) == 0:
        return []

    for i in range(len(container) - 1, 0, -1):
        is_sorted = True

        for j in range(i):
            if container[j] > container[j + 1]:
                container[j], container[j + 1] = container[j + 1], container[j]
                is_sorted = False
        
        if is_sorted:
            break