def solution(lines):
    # 입력 표현 변경
    new_lines = []
    for line in lines:
        end, during = line.split()[1:]
        end = end.split(':')
        end = int(end[0]) * 3600 + int(end[1]) * 60 + float(end[2])
        during = float(during.rstrip('s'))
        new_lines.append([end - during + 0.001, end])

    # new_lines.sort(key=lambda x: (x[1], x[0]))
    answer = 1
    for i, line in enumerate(new_lines):
        end = line[1] + 1 - 0.001
        temp = 1
        for j in range(i+1, len(new_lines)):
            # 부동 소숫점 에러 엡실론
            if end - new_lines[j][0] > - 0.0000001:
                temp += 1
        if answer < temp:
            answer = temp            
    return answer