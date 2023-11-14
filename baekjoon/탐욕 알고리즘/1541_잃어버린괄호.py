import sys
input = sys.stdin.readline

# 완전 탐색 알고리즘
def solution_recursive(numbers, expressions):
    if len(numbers) == 1:   # 기저사례 숫자가 하나 남은 경우
        return numbers[-1]
    
    e = expressions[0]
    cur, next = numbers[0], numbers[1]
    # 연산에 따라 최소값 구하기
    if e == '-':
        ret = min(
            solution_recursive([cur - next] + numbers[2:], expressions[1:]), 
            cur - solution_recursive(numbers[1:], expressions[1:])
        )
    else:   
        ret = min(
            solution_recursive([cur + next] + numbers[2:], expressions[1:]), 
            cur + solution_recursive(numbers[1:], expressions[1:])
        )
        
    return ret

# EXPRESS = '+-'
# string = input()
# numbers = list()
# expressions = list()
# temp = ''
# for s in string:
#     if s in EXPRESS:
#         expressions.append(s)
#         numbers.append(int(temp))
#         temp = ''
#     else:
#         temp += s
# numbers.append(int(temp))
# print(solution_recursive(numbers, expressions))


# 그리디
def solution(expressions):
    expressions = expressions.split('-')
    ret = sum([int(num) for num in expressions[0].split('+')])  # 초기값 설정
    for e in expressions[1:]:   # 나머지 부분 순회하며 계산하기
        for n in e.split('+'):
            ret -= int(n)
        
    return ret


expressions = input()
print(solution(expressions))