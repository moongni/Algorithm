def solution(name):
    answer = 0
    min_move = len(name) - 1
    for i in range(len(name)):
        # 알파벳 이동
        answer += min(ord(name[i]) - 65, 91 - ord(name[i]))

        # 왼쪽 오른쪽 중 가장 짧은 이동
        idx = i + 1
        while idx < len(name) and name[idx] == 'A':
            idx += 1
        
        # 오른쪽 또는 왼쪽 순해 min_move
        # 오른쪽 이동 후 왼쪽 i * 2 + len(name) - idx
        # 왼쪽 이동 후 오른쪽 i + 2 * (len(name) - idx)
        min_move = min([min_move, i * 2 + len(name) - idx, i + 2 * (len(name) - idx)])
        
    answer += min_move
    return answer