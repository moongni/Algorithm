import sys

input = sys.stdin.readline

N = int(input())
k = int(input())

ret = 0
start = 1
end = k
while start <= end:
    mid = (start + end) // 2
    
    cnt = 0
    for i in range(1, N + 1):
        cnt += min(mid // i, N)
    
    if cnt < k:
        start = mid + 1
    else:
        ret = mid
        end = mid - 1

print(ret)