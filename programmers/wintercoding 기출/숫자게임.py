def solution(A, B):
    A.sort()
    B.sort()
    answer = 0
    for i in range(len(A) - 1, -1, -1):
        if len(B) > 0 and A[i] < B[-1]:
            answer += 1
            B.pop()
                
    return answer