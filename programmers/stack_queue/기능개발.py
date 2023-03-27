def solution(progresses, speeds):
    # 남은 일정 구하기
    remain = []
    for i in range(len(progresses)):
        temp = -((progresses[i] - 100) // speeds[i])
        remain.append(temp)

    # 개수 구하기
    answer = []
    cnt = 1
    pred = remain.pop(0)
    while len(remain) != 0:
        next = remain.pop(0)

        if pred >= next:
            cnt += 1
        else:
            answer.append(cnt)
            pred = next
            cnt = 1
    answer.append(cnt)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))
print(-((30 - 100) // 30))