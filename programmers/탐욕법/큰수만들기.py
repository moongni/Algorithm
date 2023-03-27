import sys
sys.setrecursionlimit(1000000)
# 앞자리부터 큰수남기기
# 문자열 슬라이싱이 많아서 시간초과??
def solution(number, k):
    answer = ''
    len_number = len(number)
    start = 0
    while k != 0 and len_number - start != k:
        max_first = '0'
        step = 0
        for i in range(k+1):
            if max_first < number[start + i]:
                max_first = number[start + i]
                step = i
                if max_first == '9':
                    break
        answer += max_first
        start += step + 1
        k -= step

    if k == 0:
        answer += number[start:]
    return answer


import sys
sys.setrecursionlimit(1000000)
# 앞자리부터 큰수남기기
def solution(number, k):
    # 기저사례: 더 뺄 수 없으면 number 반환
    if k == 0: 
        return number
    # 기저사례: 나머지 number 다 뺴기
    if len(number) == k:
        return ''

    max_first = '0'
    max_idx = 0
    for i in range(k+1):
        if max_first < number[i]:
            max_first = number[i]
            max_idx = i
            if max_first == '9':
                break

    return max_first + solution(number[max_idx + 1:], k - max_idx)
