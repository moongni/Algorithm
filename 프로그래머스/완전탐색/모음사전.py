WORD = ['A', 'E', 'I', 'O', 'U']

def solution(word):
    answer = 0
    curr_word = ''
    word_idx = 0
    while True:
        if len(curr_word) != 5:
            word_idx = 0
            curr_word += WORD[word_idx % 5]
        else:
            while curr_word[-1] == 'U':
                curr_word = curr_word[:-1]
                word_idx = WORD.index(curr_word[-1])
            word_idx += 1
            curr_word = curr_word[:-1] + WORD[word_idx % 5]
        answer += 1

        if curr_word == word:
            return answer
print(solution("UUUUU"))

from itertools import product

solution = lambda word: sorted(["".join(c) for i in range(5) for c in product("AEIOU", repeat=i+1)]).index(word) + 1
