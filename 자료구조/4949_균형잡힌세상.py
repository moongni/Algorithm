import sys

input = sys.stdin.readline

while True:
    string = input().rstrip()
    if string == '.':
        break

    stack = []
    is_balanced = True
    for s in string:
        if s in '([':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else: 
                is_balanced = False
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else: 
                is_balanced = False
                break
    print('yes' if is_balanced and len(stack) == 0 else 'no')