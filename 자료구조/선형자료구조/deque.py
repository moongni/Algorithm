"""
    선형자료구조 - 덱
    덱은 큐와 유사하게 작용하지만 큐와 달리 항목의 추가와 삭제가 머리와 꼬리 양쪽에서
    모두 처리한다. 덱은 큐와 스택의 기능을 함께 제공한다.
"""

class Deque:
    def __init__(self):
        self.container = []
    
    def __repr__(self) -> str:
        return f"<{self.container}>"
    
    def is_empty(self):
        return not bool(self.container)

    # 머리 쪽 처리
    def add_front(self, item):
        self.container.insert(0, item)
    
    def remove_front(self):
        return self.container.pop(0)

    # 꼬리 쪽 처리
    def add_rear(self, item):
        self.container.append(item)
    
    def remove_rear(self):
        return self.container.pop()
    
    def size(self):
        return len(self.container)

# 테스트
if __name__ == "__main__":
    d=Deque()
    print(d.is_empty())
    d.add_rear(4)
    d.add_rear('dog')
    d.add_front('cat')
    d.add_front(True)
    print(d)
    print(d.size())
    print(d.is_empty())
    d.add_rear(8.4)
    print(d.remove_rear())
    print(d.remove_front())
    print(d)