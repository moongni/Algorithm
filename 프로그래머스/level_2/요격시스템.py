def solution(targets):
    targets.sort(key=lambda x: (x[1], x[0]))
    answer = 0
    end = 0
    for i in range(len(targets)):
        if end <= targets[i][0]:
            answer += 1
            end = targets[i][1]
        
    return answer