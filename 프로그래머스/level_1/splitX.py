def solution(s):
    answer = 0
    cntx = 0
    cntn = 0

    for ch in s:
        if cntx == cntn:
            answer += 1
            x = ch
        
        if x == ch:
            cntx += 1
        else:
            cntn += 1

    return answer

print(solution("banana"))
print(solution("abracadabra"))
print(solution("aaabbaccccabba"))
print(solution(""))