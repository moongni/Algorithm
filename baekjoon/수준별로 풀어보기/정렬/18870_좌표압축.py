def solution(arr):
    new_arr = []
    sorted_arr = sorted(arr, reverse=True)
    for item in arr:
        idx = sorted_arr.index(item)
        n = len(set(sorted_arr[idx:]))    
        new_arr.append(n - 1)
    return new_arr    

n = int(input())
arr = list(map(int, input().split()))
new_arr = solution(arr)
print(' '.join(map(str, new_arr)))