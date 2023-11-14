def solution(S):
    # 연속된 0과 1의 수를 저장
    reverse = [0, 0]
    # 첫번째 요소를 저장
    prev = S[0]
    reverse[prev] += 1
    for i in range(1, len(S)):
        # 연속된 수일 경우 제외
        if prev == S[i]:
            continue
        # 수가 반전되었을 경우
        reverse[S[i]] += 1
        prev = S[i]
        
    return min(reverse) # 저장된 수 중 작은 값을 반환
    
S = [int(s) for s in input()]
result = solution(S)
print(result)