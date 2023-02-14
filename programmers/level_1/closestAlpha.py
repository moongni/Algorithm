def solution(s):
    answer = []
    hash_ = {}

    for i in range(len(s)):
        if s[i] in hash_:
            answer.append(i - hash_[s[i]])
        else:
            answer.append(-1) 

        hash_[s[i]] = i           

    return answer

print(solution("banana"))