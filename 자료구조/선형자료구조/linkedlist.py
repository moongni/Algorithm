"""
    선형자료구조 - 연결 리스트
    배열의 경우 인덱스를 통해 빠른 접근이 가능하지만
    추가와 삭제의 경우 시간복잡도가 증가하는 경향이 있다.

    연결리스트는 배열의 단점을 개선하기 위해 생긴 자료구조이다.
    기본적인 구조는 아래와 같다.
    Node - 데이터와 다음 데이터를 가르키는 주소(포인터)로 구성
    Pointer - 각 노드에서 다음 데이터를 가르키는 주소값
    Head - 연결리스트의 시작점 데이터
    Tail -연결리스트의 마지막 데이터
    Next - 다음 데이터를 말하며 없을경우 None or null 값

    장점
    배열의 경우 데이터 공간을 할당해야 하지만 연결리스트는 미리 할당할 필요없다.
    수정시에 시간복잡도 O(1)을 가짐

    단점
    다음 데이터를 연결하기 위해 별도의 주소 공간을 가져야함 -> 저장공간 효율이 좋지 않다
    데이터에 접근하는 경우 O(n)의 복잡도를 가짐
    중간데이터를 삭제 시, 앞뒤 데이터를 연결하는 재구성코드가 필요
"""

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
    
    def __repr__(self):
        return f"data: {self.data}\n{self.next}"
    
    # 맨 뒤에 노드 추가
    def append(self, node):
        curr = self

        while curr.next != None:
            curr = curr.next
        
        curr.next = node

    # 인덱스로 노드 추가
    def insert(self, node, idx=-1):
        # 디폴트 맨뒤에 추가
        if idx == -1:
            curr = self

            while curr.next:
                curr = curr.next
            
            curr.next = node
        else:
            curr = self

            for _ in range(idx - 1):
                if curr != None:
                    curr = curr.next            

            node.next = curr.next
            curr.next = node
    
    # 인덱스로 노드 제거
    def remove_by_idx(self, idx = -1):
        # 디폴트 맨뒤에 링크 제거
        if idx == -1:
            curr, pred = self, None

            while curr.next:
                curr, pred = curr.next, curr
            
            pred.next = None
        else:
            curr, pred = self, None

            for _ in range(idx):
                if curr != None:
                    curr, pred = curr.next, curr
                
            pred.next = curr.next

    # 값으로 노드 제거
    def remove_by_value(self, value):
        curr = self

        while curr.next:
            if curr.next.data == value:
                curr.next = curr.next.next
                break
            
            curr = curr.next
        
    # 연결 리스트 뒤집기
    def reverse(self):
        curr, revd = self, None

        while curr:
            next, curr.next = curr.next, revd
            revd, curr = curr, next

        return revd
            
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)

n1.append(n2)
n1.append(n3)
n1.append(n4)
n1.append(n5)

print(n1.reverse())