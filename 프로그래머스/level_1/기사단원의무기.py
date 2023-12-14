"""
    기사단원의무기
"""
def solution(number, limit, power):
    def get_measure(num):
        measure = 0

        for i in range(1, int(num**(1/2)) + 1):
            if num % i == 0:
                measure += 2
            if i * i == num:
                measure -= 1

            # limit 초과시 power
            if measure > limit:
                return power

        return measure

    anwser = sum([get_measure(i) for i in range(1, number + 1)])

    return anwser