"""
    n개의 원소 중 m개를 고르는 모든 조합을 찾는 알고리즘
"""

from typing import List

def pick(n: int, pick_list: List[int], picked: List[int], to_pick: int) -> None:
    """
        paremter:
            n: int 전체 원소의 수
            picked: 이미 고른 원소의 인덱스 리스트
            to_pick: int 더 골라야되는 원소의 수
    """
    
    if to_pick == 0:
        for i in picked:
            print(pick_list[i], end=' ')
        print()
        return 0
    
    # 마지막 인덱스 찾기
    last_idx = 0
    if len(picked) != 0:
        last_idx = picked[-1] + 1
    
    for i in range(last_idx, n):
        picked.append(i)
        pick(n, pick_list, picked, to_pick - 1)
        picked.pop()


testList = [ i for i in range(7)]
pick(7, testList, [], 4)
