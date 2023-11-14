import sys

input = sys.stdin.readline

N, M, R = map(int, input().split())
# nlogn
pillars = list(map(int, input().split()))
flags = sorted(list(map(int, input().split())), reverse=True)
square_R = R * 2

# n**2
bases = set()
for i in range(len(pillars)):
    for j in range(i + 1, len(pillars)):
        bases.add(abs(pillars[j] - pillars[i]))

# n*m
answer = -1
for base in bases:
    for flag in flags:
        area = base * flag
        if area > square_R:
            continue
        answer = max(answer, round(area / 2, 1))
        break
print(answer)