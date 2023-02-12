"""
    최대 증가 부분 수열 계산하기
    최대 증가 부분 수열의 경로를 반환하는 함수
"""

cache = [-1] * 10
choices = [-1] * 10

def lis4(S, start=-1):
    if start == -1:
        maxLen = 0
        for i in range(0, len(S)):
            maxLen = max(maxLen, lis4(S, i))

        return maxLen
    else:
        #기저사례: 메모이제이션
        if cache[start] != -1:
            return cache[start]

        # S[start]은 항상 존재하기 때문에 1
        cache[start] = 1
        bestNet = 1

        for i in range(start, len(S)):
            if S[start] < S[i]:
                cand = lis4(S, i) + 1
                if cand > cache[start]:
                    cache[start] = cand
                    bestNet = i
        choices[start] = bestNet

        return cache[start]

print(lis4([3, 2, 1, 7, 5, 4, 2, 6]))
print(cache)
print(choices)