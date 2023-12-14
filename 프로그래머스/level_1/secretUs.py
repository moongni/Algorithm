def solution(s, skip, index):
    # using dynamic programming
    not_skip = [c for c in range(ord('a'), ord('z') + 1) if chr(c) not in skip]    
    cache = [-1] * 26

    # 동적알고리즘 사용
    def secret(start):
        # basecase: s의 끝까지 변환
        if start == len(s):
            return ""

        # cache 접근용
        idx = ord(s[start]) - 97

        # memoization
        if cache[idx] != -1:
            return chr(cache[idx]) + secret(start + 1)

        # change string
        cache[idx] = not_skip[(not_skip.index(ord(s[start])) + index) % len(not_skip)]

        return chr(cache[idx]) + secret(start + 1)

    answer = secret(0)
            
    return answer

# print(solution("z", "abcdefghij", 20))
# print(solution("aukks", "wbqd", 5))