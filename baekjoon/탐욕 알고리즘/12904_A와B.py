import sys

input = sys.stdin.readline

S = list(input().rstrip())
T = list(input().rstrip())

while len(T) > len(S):
    if T[-1] == 'A':
        T.pop()
    else:
        T.pop()
        T = T[::-1]
        
print(1 if T == S else 0)