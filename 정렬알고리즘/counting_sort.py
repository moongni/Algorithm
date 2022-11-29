from typing import List

def counting_sort(container: List[int]) -> List[int]:
    """
        parameter:
            container: List[int] : 정렬할 배열

        ----------------------

        return:
            정렬된 배열
        
        ----------------------
        시간복잡도 O(n: len(container) + k: max_value)
        k가 커질 수록 k가 시간복잡도를 지배
        
    """
    max_value = max(container)
    sorted_list = [-1] * len(container)
    counting_list = [0] * (max_value + 1)
    
    # 배열의 값 세기
    for item in container:
        counting_list[item] += 1
    
    # 누적합 계산
    for i in range(max_value):
        counting_list[i + 1] += counting_list[i]
    
    for j in range(len(container) - 1, -1, -1):
        sorted_list[counting_list[container[j]] - 1] = container[j]
        counting_list[container[j]] -= 1
    
    return sorted_list