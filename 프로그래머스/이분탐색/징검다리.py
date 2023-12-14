def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)

    left, right = 1, distance

    while left <= right:
        mid = (left + right) // 2
        curr = 0
        removed = 0
        min_distance = float('inf')
        for rock in rocks:
            diff = rock - curr
            if diff < mid:
                removed += 1
            else:
                curr = rock
                min_distance = min(min_distance, diff)
        
        if removed > n:
            right = mid - 1
        else:
            answer = min_distance
            left = mid + 1
    
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))
