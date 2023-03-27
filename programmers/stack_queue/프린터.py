def solution(priorities, location):
    answer = 0
    while len(priorities) != 0 and location >= 0:
        curr = priorities.pop(0)
        location -= 1

        # 스케줄링 
        if any(curr < prior for prior in priorities):
            priorities.append(curr)
            if location < 0:
                location = len(priorities) - 1
        else:
            answer += 1  
    return answer

print(solution([1, 9, 1, 1, 1, 1], 0))

def solution(priorities, location):
    queue =  [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                return answer
