import sys

input = sys.stdin.readline

N, M, K = map(int, input().split())
nums = [0] + [int(input()) for _ in range(N)]
commands = [list(map(int, input().split())) for _ in range(M + K)]


class SegTree:
    def __init__(self):
        self.tree = [0] * (4 * N)
        self.init(1, N)

    def init(self, start, end, node=1):
        # leaf node의 경우
        if start == end:
            self.tree[node] = nums[start]
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = self.init(start, mid, node * 2) \
            + self.init(mid + 1, end, node * 2 + 1)
        return self.tree[node]

    def get_sum(self, start, end, left, right, node=1):
        # 범위를 벗어날 경우
        if left > end or right < start:
            return 0
        # 범위 내에 존재할 경우
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return self.get_sum(start, mid, left, right, node * 2) \
            + self.get_sum(mid + 1, end, left, right, node * 2 + 1)

    def update(self, start, end, index, dif, node=1):
        # 범위를 벗어난 경우
        if index < start or end < index:
            return
        # dif만큼 업데이트
        self.tree[node] += dif
        # leaf node의 경우
        if start == end:
            return

        mid = (start + end) // 2
        self.update(start, mid, index, dif, node * 2)
        self.update(mid + 1, end, index, dif, node * 2 + 1)

    def __str__(self):
        return str(self.tree)


seg_tree = SegTree()
for comm in commands:
    if comm[0] == 1:
        seg_tree.update(1, N, comm[1], comm[2] - nums[comm[1]])
        nums[comm[1]] = comm[2]
    else:
        print(seg_tree.get_sum(1, N, comm[1], comm[2]))
