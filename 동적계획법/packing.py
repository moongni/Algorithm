"""
    짐싸기 문제
    물건, 부피, 절박도가 주어진 상황에서 케리어의 부피 W를 초과하지 않으며 절박도가 제일 높은 조합의 물건을 반환하라.
"""
import printBoard

# W이내에 절박도를 cache에 저장하여 절박도를 반환하는 함수
def packing(item, capacity):
    # 기저조건: 모든 아이템을 선택한 경우
    if item == n: return 0
    
    # 메모이제이션
    if cache[item][capacity] != -1:
        return cache[item][capacity]

    # 현재 물건을 담지 않는 경우
    cache[item][capacity] = packing(item + 1, capacity)

    # 현재 물건을 담는 경우
    if capacity >= volumns[item]:
        cache[item][capacity] = max(cache[item][capacity],
                                    packing(item + 1, capacity - volumns[item]) + needs[item])

    return cache[item][capacity]

# 선택한 아이템을 역추적하는 프로그램
def reconstruct(item, capacity, picked):
    # 기저사례: 모든 아이템을 고려함
    if item == n: return 0

    if packing(item, capacity) == packing(item + 1, capacity):
        reconstruct(item + 1, capacity, picked)
    else:
        picked.append(items[item])
        reconstruct(item + 1, capacity - volumns[item], picked)

# 예제 1    
# n: 물건의 갯수 / w: 캐리어의 부피
n = 6; w = 10

items = ["laptop", "camera", "xbox", "grinder", "dumbell", "encyclopedia"]
volumns = [4, 2, 6, 4, 2, 10]
needs = [7, 10, 6, 7, 5, 4]

cache = [[-1 for i in range(w + 2)] for i in range(n + 2)]
picked = []

reconstruct(0, w, picked)
print(picked)

# 예제 2    
n = 6; w = 17

cache = [[-1 for i in range(w + 2)] for i in range(n + 2)]
picked = []

reconstruct(0, w, picked)
print(packing(0, w), len(picked))
print(picked)