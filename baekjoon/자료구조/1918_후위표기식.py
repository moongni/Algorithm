import sys

input = sys.stdin.readline


operator_priority = {
    '+': 3,
    '-': 3,
    '*': 2,
    '/': 2,
    '(': 1,
    ')': 1
}

def main(expression):
    ret = ""
    stack = list()
    for e in expression:
        if e in operator_priority:
            # )일 경우 (가 나올때까지 결과에 추가
            if e == ')':
                while stack[-1] != '(':
                    ret += stack.pop()
                stack.pop()
                continue
            
            # 최근 연산지 우선순위 비교하여 우선순위가 더 높다면 결과에 추가
            while stack and stack[-1] != '(' and operator_priority[stack[-1]] <= operator_priority[e]:
                ret += stack.pop()
                
            stack.append(e)
            
        # 연산자가 아닌 경우
        else:
            ret += e
    
    while stack:
        s = stack.pop()
        if s != '(':
            ret += s
            
    return ret


expression = input().strip()


if __name__ == "__main__":
    print(main(expression))