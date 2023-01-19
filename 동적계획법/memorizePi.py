"""
    원주율 외우기
    원주율을 3자리 또는 5자리씩 끊으려고 할 때 아래 규칙에서 난이도가 가장 적도록 끊는 경우의 난이도를 찾아라
    1. 모든 숫자가 같을 때 333, 55555 - 난이도 1
    2. 숫자가 1씩 증가 또는 감소 123, 54321 - 난이도 2
    3. 두 개의 숫자가 번갈아 나올 때 323, 54545 - 난이도 4
    4. 숫자가 등차 수열일 때 147, 8642 - 난이도 5
    5. 이 외 모든 경우 - 난이도 10

    입력
    첫 줄 테스트 케이스 1<= C <=50
    각 테스트 케이스 8<= c <= 10,000
"""

def recursive_pi(s, start=0):
    # 기저조건: start == len(s)
    if start == len(s):
        return 0

    # 기저조건: 남은 수열의 수가 3이하인 경우
    if start + 3 > len(s):
        return float("inf")

    ret = float("inf")
    
    for i in range(3, 6):
        i = min(i, len(s) - start)

        # 기본 10
        level = 10

        # 4. 등차 수열
        flag4 = True
        differ = s[start] - s[start + 1]
        for sub_idx in range(start + 2, start + i):
            if differ != s[sub_idx-1] - s[sub_idx]:
                flag4 = False

        if flag4:
            level = 5

        # 3. 숫자가 번갈아 나올 때
        flag3 = True
        for sub_idx in range(start + 2, start + i):
            if s[sub_idx - 2] != s[sub_idx]:
                flag3 = False
        
        if flag3:
            level = 4

        # 2. 단조 증가 감소
        flag2 = True
        differ2 = s[start] - s[start + 1]

        if differ2**2 != 1:
            flag2 = False

        for sub_idx in range(start + 2, start + i):
            if s[sub_idx - 1] - s[sub_idx] != differ:
                flag2 = False
            
        if flag2:
            level = 2
        
        # 1. 모두 같은 수
        flag1 = True
        first = s[start]
        for sub_idx in range(start + 1, start + i):
            if first != s[sub_idx]:
                flag1 = False
        
        if flag1:
            level = 1
        
        ret = min(ret, level + recursive_pi(s, start + i))
    
    return ret

# print(recursive_pi([1,2,3,4,1,2,3,4]))
# print(recursive_pi([1,1,1,1,1,2,2,2]))
# print(recursive_pi([1,2,1,2,2,2,2,2]))
# print(recursive_pi([2,2,2,2,2,2,2,2]))
# print(recursive_pi([1,2,6,7,3,9,3,9]))

def dynamic_pi(s, start=0):
    # 기저사례
    # s의 마지막에 도달
    if len(s) == start:
        cache[start] = 0
        return cache[start]

    # 남은 s가 3개 이하일 경우    
    if start + 3 > len(s):
        cache[start] = float("inf")
        return float("inf")

    # 메모이제이션
    if cache[start] != float("inf"):
        return cache[start]

    # 최저 난이도 찾기
    for i in range(3, 6):
        i = min(i, len(s) - start)

        # 기본 10
        level = 10

        # 4. 등차 수열
        flag4 = True
        differ = s[start] - s[start + 1]
        for sub_idx in range(start + 2, start + i):
            if differ != s[sub_idx-1] - s[sub_idx]:
                flag4 = False

        if flag4:
            level = 5

        # 3. 숫자가 번갈아 나올 때
        flag3 = True
        for sub_idx in range(start + 2, start + i):
            if s[sub_idx - 2] != s[sub_idx]:
                flag3 = False
        
        if flag3:
            level = 4

        # 2. 단조 증가 감소
        flag2 = True
        differ2 = s[start] - s[start + 1]

        if differ2**2 != 1:
            flag2 = False

        for sub_idx in range(start + 2, start + i):
            if s[sub_idx - 1] - s[sub_idx] != differ:
                flag2 = False
            
        if flag2:
            level = 2
        
        # 1. 모두 같은 수
        flag1 = True
        first = s[start]
        for sub_idx in range(start + 1, start + i):
            if first != s[sub_idx]:
                flag1 = False
        
        if flag1:
            level = 1
        
        cache[start] = min(cache[start], level + dynamic_pi(s, start + i))
    
    return cache[start]

# cache = [float("inf")] * 9
# print(dynamic_pi([1,2,3,4,1,2,3,4]))
# print(cache)
# cache = [float("inf")] * 9
# print(dynamic_pi([1,1,1,1,1,2,2,2]))
# print(cache)
# cache = [float("inf")] * 9
# print(dynamic_pi([1,2,1,2,2,2,2,2]))
# print(cache)
# cache = [float("inf")] * 9
# print(dynamic_pi([2,2,2,2,2,2,2,2]))
# print(cache)
# cache = [float("inf")] * 9
# print(dynamic_pi([1,2,6,7,3,9,3,9]))
# print(cache)

# ======================================== #
# 책 해설
# 난이도 측정 함수
def classify(s, start, end):
    # 숫자 조각 슬라이싱
    m = s[start: end + 1]

    # 한글자로 이뤄진 문자열 난이도 1
    allsame = True
    for i in range(len(m)):
        if m[i] != m[0]:
            allsame = False

    if allsame: return 1        

    # 등차수열 확인
    progressive = True
    for i in range(len(m) - 1):
        if m[i + 1] - m[i] != m[1] - m[0]:
            progressive = False
    
    # 등차수열이 1 또는 -1 일때 난이도 2
    if progressive and (m[1] - m[0])**2 == 1:
        return 2
    
    # 두 수가 번갈아 나오는 경우
    alternating = True
    for i in range(len(m)):
        if m[i] != m[i % 2]:
            alternating = False

    if alternating: return 4
    if progressive: return 5

    return 10

def dynamic_pi2(s, start=0):
    # 기저 사례: 수열의 끝에 도달
    if len(s) == start:
        cache[start] = 0
        return cache[start]
    
    # 메모이제이션
    if cache[start] != -1:
        return cache[start]
    
    cache[start] = float("inf")

    for l in range(3, 6):
        if start + l <= len(s):
            cache[start] = min(cache[start], \
                dynamic_pi2(s, start + l) + classify(s, start, start + l - 1))
            
    return cache[start]

cache = [-1] * 9
print(dynamic_pi2([1,2,3,4,1,2,3,4]))
print(cache)
cache = [-1] * 9
print(dynamic_pi2([1,1,1,1,1,2,2,2]))
print(cache)
cache = [-1] * 9
print(dynamic_pi2([1,2,1,2,2,2,2,2]))
print(cache)
cache = [-1] * 9
print(dynamic_pi2([2,2,2,2,2,2,2,2]))
print(cache)
cache = [-1] * 9
print(dynamic_pi2([1,2,6,7,3,9,3,9]))
print(cache)

# 나와 다른점
# 남은 s가 3개 이하인 경우을 생략하는 방식
# 점수를 낮은 점수를 우선으로 반환하여 계산의 수를 줄이는 방식
# classify 함수를 min 함수 내부에 선언함으로써 코드 가독성을 늘리는 방식
