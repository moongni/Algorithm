def solution(land, P, Q):
    N = len(land)
    arr = []
    for i in range(N):
        for j in range(N):
            arr.append(land[i][j])
    arr.sort()
    n = len(arr)
    
    answer = removed = (sum(arr) - arr[0] * n) * Q
    prev_height = arr[0]
    fill = 0
    for i in range(1, N ** 2):
        if arr[i - 1] == arr[i]:
            continue
        
        fill += (arr[i] - prev_height) * i * P
        removed -= (arr[i] - prev_height) * (n - i) * Q
        cost = fill + removed
        answer = min(answer, cost)
        prev_height = arr[i]

    return answer
        