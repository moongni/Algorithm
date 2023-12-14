def solution(cookie):
    answer = 0
    for i in range(len(cookie) - 1):
        first_son = [cookie[i]]
        for f in range(i - 1, -1, -1):
            first_son.append(first_son[-1] + cookie[f])
        second_son = [cookie[i + 1]]
        for s in range(i + 2, len(cookie)):
            second_son.append(second_son[-1] + cookie[s])
            
        intersection = set(first_son).intersection(set(second_son))
        if intersection:
            answer = max(answer, max(intersection))
    
    return answer