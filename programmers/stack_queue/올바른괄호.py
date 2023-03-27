def solution(s):
    stack = []

    for ch in s:
        if ch == "(":
            stack.append(ch)
        else:
            if stack[-1:] == ["("]:
                stack.pop()
            else:
                stack.append(ch)

    return len(stack) == 0