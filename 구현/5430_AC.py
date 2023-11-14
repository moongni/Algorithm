import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P = input().rstrip()
    N = int(input())
    arr = deque()
    items = input().rstrip()
    string = ''
    for i in range(1, len(items) - 1):
        s = items[i]
        if s == ',':
            arr.append(string)
            string = ''
        else:
            string += s
    if string:
        arr.append(string)
        
    is_error = False
    is_reverse = False
    for p in P:
        if p == 'R':
            is_reverse = not is_reverse
        else:
            if is_reverse:
                if arr:
                    arr.pop()
                else:
                    is_error = True
                    break
            else:
                if arr:
                    arr.popleft()
                else:
                    is_error = True
                    break
    arr = list(arr)
    if is_error:
        print('error')
    else:
        if is_reverse:
            string = ','.join(arr[::-1])
        else:
            string = ','.join(arr)
        print(f"[{string}]")