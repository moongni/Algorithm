import sys

input = sys.stdin.readline

N, M = map(int, input().split())
trees = list(map(int, input().split()))

ret = 0
# 총 탐색구간 설정
start, end = 0, max(trees)
while start <= end:
    mid = (start + end) // 2
    total_tree = sum([tree - mid for tree in trees if tree > mid])
    # 탐색 구간 재설정
    if total_tree < M:
        end = mid - 1
    else:
        ret = mid
        start = mid + 1
print(ret)