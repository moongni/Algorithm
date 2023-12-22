import sys

input = sys.stdin.readline

N, K = map(int, input().split())
items = [list(map(int, input().split())) for _ in range(N)]
items.sort(key=lambda x: (x[0], x[1]))

bags = [[0] * (K + 1) for _ in range(N + 1)]
for n in range(1, N + 1):
    item_idx = n - 1
    for weight in range(1, K + 1):
        if items[item_idx][0] <= weight:
            bags[n][weight] = max(
                bags[n - 1][weight],
                bags[n - 1][weight - items[item_idx][0]] + items[item_idx][1]
            )
        else:
            bags[n][weight] = bags[n - 1][weight]

print(bags[-1][-1])