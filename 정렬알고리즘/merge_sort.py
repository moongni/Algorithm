from typing import List

def merge_sort(container: List[int]) -> None:
    '''
        parameter:
        container: List[int] 정렬하기 희망하는 리스트

        ------------------

        리스트를 절반으로 분할하여 정렬하며 합병

    '''
    if len(container) > 1:
        # 분할
        half = len(container) // 2
        left_list = container[ : half]
        right_list = container[half : ]
        merge_sort(left_list)
        merge_sort(right_list)

        # 합병
        i, j, k = 0, 0, 0

        while i < len(left_list) and j < len(right_list):
            if left_list[i] <= right_list[j]:
                container[k] = left_list[i]
                i += 1
            else:            
                container[k] = right_list[j]
                j += 1
            
            k += 1
        
        while i < len(left_list):
            container[k] = left_list[i]
            i += 1
            k += 1
        
        while j < len(right_list):
            container[k] = right_list[j]
            j += 1
            k += 1
    