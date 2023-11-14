import sys

input = sys.stdin.readline

# Linked List
class Node:
    def __init__(self, num=None):
        self.num = num
        self.next = None
        
class SortedLinkedList:
    def __init__(self):
        self.first = Node()
        self.len = 0
    
    def insert(self, node: Node):
        prev_node = self.first
        cur_node = self.first.next
        while cur_node is not None:
            if node.num > cur_node.num:
                prev_node = cur_node
                cur_node = cur_node.next
            else:
                break
            
        node.next = cur_node
        prev_node.next = node
        self.len += 1
            
    def popleft(self) -> int:
        node = self.first.next
        if node is not None:
            self.first.next = node.next
        self.len -= 1
        return node.num
    
    def __len__(self):
        return self.len
            
T = int(input())
min_value = 1_000_000_007
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    
    linked_list = SortedLinkedList()
    for num in nums:
        linked_list.insert(Node(num))
        
    cost = 1
    while len(linked_list) > 1:
        min_n, max_n = linked_list.popleft(), linked_list.popleft()
        new_num = min_n * max_n
        cost *= new_num
        linked_list.insert(Node(new_num))
    print(cost % min_value)
    
# deque
import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
min_value = 1_000_000_007
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    nums = deque(sorted(nums))
    cost = 1
    while len(nums) > 1:
        min_n, max_n = nums.popleft(), nums.popleft()
        new_num = min_n * max_n
        cost *= new_num
        for i in range(len(nums)):
            if new_num < nums[i]:
                nums.insert(i, new_num)
                break
        else:
            nums.append(new_num)
    print(cost % min_value)
    
    
# heapq
import sys
import heapq

input = sys.stdin.readline

T = int(input())
min_value = 1_000_000_007

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    heapq.heapify(nums)
    cost = 1
    while len(nums) > 1:
        min_n, max_n = heapq.heappop(nums), heapq.heappop(nums)
        new_num = min_n * max_n
        cost *= new_num
        heapq.heappush(nums, new_num)
        
    print(cost % min_value)


