def solution(people, limit):
    answer = 0
    people.sort(reverse=True)

    left = 0
    right = len(people) - 1
    while left < right:
        if people[left] + people[right] > limit:
            left += 1
        else:
            left += 1
            right -= 1
        answer += 1
    if left == right:
        answer += 1                

    return answer

solution([70, 50, 80, 50], 100)