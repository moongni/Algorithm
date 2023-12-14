def solution(n, words):
    answer = [0, 0]
    last_word = words[0][-1]
    for i in range(1, len(words)):
        cur_word = words[i]
        if last_word != cur_word[0] or cur_word in words[:i]:
            answer[0] = (i % n) + 1
            answer[1] = i // n + 1
            break
        last_word = cur_word[-1]
    return answer
