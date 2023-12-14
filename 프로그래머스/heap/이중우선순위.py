import heapq as hq

def solution(operations):
    answer = []
    
    for oper in operations:
        operation, item = oper.split()

        if operation == 'I':
            hq.heappush(answer, int(item))
        elif answer:
            if item == '-1':
                hq.heappop(answer)
            else:
                answer.pop()
        
        # 가장 큰 밸류를 맨 뒤로 보내기 feat 버블 소트
        for i in range(len(answer) - 1):
            if answer[i] > answer[i+1]:
                answer[i], answer[i+1] = answer[i+1], answer[i]

    if not answer:
        return [0, 0]
    
    return [answer[-1], answer[0]]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))

print(int('-45'))
print(solution( ["I 4", "I -1", "I 6", "I 3"] ))