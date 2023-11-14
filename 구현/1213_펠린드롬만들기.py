import sys
input = sys.stdin.readline

alphabats = list(input().strip('\n'))

def get_palindrome(alpha):
    alpha.sort()
    # 알파벳 순으로 정렬된 카운터
    counter = []
    prev_char = None
    for a in alpha:
        if prev_char != a:
            counter.append([a, 1])
            prev_char = a
        else:
            counter[-1][1] += 1
    
    # 최종 결과를 저장할 변수 
    ret = ''
    mid_char = ''
    for c in counter:
        if c[1] % 2 != 0:
            if mid_char:    # 펠린드롬을 만들 수 없는 경우
                return "I'm Sorry Hansoo"
            mid_char = c[0]
        ret += c[0] * (c[1] // 2)

    if mid_char:    # 중간 글자가 있는 경우
        ret += mid_char
        ret = ret + ret[:-1][::-1]
    else:           # 중간 글자가 없는 경우
        ret = ret + ret[::-1]
        
    return ret
    
print(get_palindrome(alphabats))