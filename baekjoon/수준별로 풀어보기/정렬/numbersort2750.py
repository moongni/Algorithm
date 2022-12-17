"""
    백준알고리즘 2750번 - 수 정렬하기
    N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.
    
    풀이: 입력시에 우선순위 힙 객체에 바로 넣고 맨 위에서부터 출력한다.
    
    O(nlogn)
"""

class Priority_Heap:
    def __init__(self):
        self.container = []
    
    def push(self, item):
        # 아이템 가장 뒤에 저장
        self.container.append(item)

        cur_idx = len(self.container) - 1
        parent_idx = (cur_idx - 1) // 2

        # 우선순위에 따라 재조정
        while cur_idx != 0 and item < self.container[parent_idx]:
            self.container[cur_idx] = self.container[parent_idx]

            cur_idx = parent_idx
            parent_idx = (cur_idx - 1) // 2
        
        self.container[cur_idx] = item

    def remove(self):
        # 우선순위가 가장 높은 아이템
        first = self.container[0]

        # 우선순위가 가장 낮은 아이템 저장 및 제거
        temp = self.container.pop()

        if len(self.container) == 0:
            return first

        parent = 0
        child = 1

        # 우선순위 재조정
        while child < len(self.container):
            # 왼쪽 자식과 오른쪽 자식 둘 다 존재 시 비교
            if child + 1 < len(self.container):
                if self.container[child] > self.container[child + 1]:
                    child += 1
            
            # temp가 더 작은 자식보다 작은 경우 break
            if temp < self.container[child]:
                break

            self.container[parent] = self.container[child]
            parent = child
            child = parent * 2 + 1
            
        self.container[parent] = temp

        return first

    @property
    def is_empty(self):
        return len(self.container) == 0

    def __repr__(self):
        return str(self.container)

n = int(input())

priority_heap = Priority_Heap()

for i in range(n):
    priority_heap.push(int(input()))

while not(priority_heap.is_empty):
    print(priority_heap.remove())