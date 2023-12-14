"""
    명예의 전당
    점수가 상위 k번째 안에 드는지 확인
    매일 마지막 점수를 answer에 append
"""
def solution(k, score):
    answer = []

    honors = []

    for s in score:
        honors.append(s)
        # 마지막 요소 앞과 비교하여 올려 제 위치
        i = len(honors) - 1
        while i > 0:
            if honors[i] > honors[i - 1]:
                honors[i], honors[i - 1] = honors[i - 1], honors[i]
            else:
                break
            i -= 1

        if len(honors) > k:
            honors.pop()
        
        answer.append(honors[-1])

    return answer

print(solution(3, [10, 100, 20, 150, 1, 100, 200]))
print(solution(4, [0, 300, 40, 300, 20, 70, 150, 50, 500, 1000]))