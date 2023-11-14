def solution(arr):
    new_arr = sorted(arr, key=lambda x: x[0])
    return new_arr

c = int(input())
arr = []
for i in range(c):
    id, name = input().split()
    arr.append((int(id), name))

new_arr = solution(arr)
for item in new_arr:
    id, name = item
    print(id, name)