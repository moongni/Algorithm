from collections import Counter

def solution(clothes):
    answer = 1
    counter = Counter(cloth[1] for cloth in clothes)

    for i in counter:
        answer *= (counter[i] + 1)

    answer -= 1

    return answer