"""
    스택 Stack
    스택 자료구조는 값들 사이의 순서가 중요한 선형 자료형이다.
    항목의 추가 삭제는 한쪽 끝에서만 허용된다.

    후입선출(LIFO) 마지막에 들어온 항목이 가장 빨리 나감

    항목의 추가 append(item) , 항목의 삭제 pop()
    시간복잡도는 O(1)
"""

class Stack:
    def __init__(self):
        self._container = []

    def __repr__(self):
        """큐 표기법: <<[1, 2, 3]>> 등등"""
        return f"<<{self._container}>>"
    
    # 스택이 비었는지 확인
    @property
    def is_empty(self):
        return not bool(self._container)

    # 항목 개수 반환    
    @property
    def size(self):
        return len(self._container)

    # 항목추가
    def push(self, item):
        self._container.append(item)
    
    # 항목 삭제
    def pop(self):
        return self._container.pop()
    
    # 항목 삭제하지 않고 마지막 항목 반환
    def peek(self):
        return self._container[-1]

# 테스트 코드
if __name__ == "__main__":
    s = Stack()

    print(s.is_empty)
    s.push(4)
    s.push("dog")
    print(s.peek())
    s.push(True)
    print(s.size)
    print(s.is_empty)
    s.push(8.4)
    print(s.pop())
    print(s.pop())
    print(s.size)