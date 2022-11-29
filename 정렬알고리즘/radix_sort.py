from typing import List
from math import log10

def radix_sort(container: List[int]) -> None:
    """
        parameter:
            container: List[int] : 정렬할 배열
        ---------------------

        return:
            None
        
    """
    max_value = max(container)

    digits = int(log10(max_value)) + 1

    radix = [[] for i in range(10)]

    for i in range(0, digits):
        digit = 10 ** i

        while len(container) != 0:
            item = container.pop(0)
            radix[item // digit % 10].append(item)
        
        for i in range(10):
            while len(radix[i]) != 0:
                container.append(radix[i].pop(0))