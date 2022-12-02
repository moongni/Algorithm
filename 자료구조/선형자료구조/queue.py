"""
    큐 Queue
    선형의 자료구조로 한쪽에서는 항목의 추가 반대편에서 항목의 삭제가 이뤄짐

    선입선출(FIFO) 먼저들어온 항목이 먼저 삭제됨

    항목의 추가 append(item) 시간복잡도 O(1)
    항목의 삭제 pop(0) 시간복잡도 O(N) N: 컨테이너 길이
    
    또는

    항목의 추가 insert(0, itme) 시간복잡도 O(N)
    항목의 삭제 pop() 시간복잡도 O(1)
"""

class Queue:
    def __init__(self):
        self._container = []
    
    def __repr__(self):
        """큐 표기법: <<[1, 2, 3]>> 등등"""
        return f"<<{self._container}>>"
    
    # 큐가 비었는지 확인
    @property
    def is_empty(self):
        return not bool(self._container)

    # 항목 개수 반환    
    @property
    def size(self):
        return len(self._container)

    # 항목추가
    def enqueue(self, item):
        self._container.append(item)
    
    # 항목 삭제
    def dequeue(self):
        return self._container.pop(0)

if __name__ == "__main__":
    q = Queue()

    print(q.is_empty)
    q.enqueue(4)
    q.enqueue("dog")
    q.enqueue(True)
    print(q.size)
    print(q.is_empty)
    q.enqueue(8.4)
    q.dequeue()
    q.dequeue()
    print(q.size)