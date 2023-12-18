import sys

input = sys.stdin.readline

n = int(input())
wines = [0] + [int(input()) for _ in range(n)]
if n == 1:
    ret = wines[1]
elif n == 2:
    ret = wines[1] + wines[2]
elif n == 3:
    ret = max(
        wines[1] + wines[2],
        wines[1] + wines[3],
        wines[2] + wines[3]
    )
else:
    max_wines = [0] * (n + 1)
    max_wines[1] = wines[1]
    max_wines[2] = wines[2] + wines[1]
    for i in range(3, n + 1):
        max_wines[i] = max(
            max_wines[i - 1],
            max_wines[i - 2] + wines[i],
            max_wines[i - 3] + wines[i - 1] + wines[i]
        )
    ret = max_wines[-1]
print(ret)