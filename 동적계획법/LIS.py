"""
    최대 증가 부분 수열 (LIS: Longest Increasing Subsequence)
    정수 수열 S의 부분 수열은 S에서 0개 이상의 숫자를 지우고 남은 수열을 말한다.
    ex : '1 2 4'는 '1 5 2 4 7'의 부분수열이다.
    
    부분 수열에 포함되는 숫자들이 순 증가 하면 이 부분 수열을 증가 부분 수열이라고 부른다.
    ex: '1 2 4'는 '1 3 4 2 4'의 증가 부분 수열이다. 
"""

# 완전탐색기법
def recursive_get_LIS(S, sub = []):
    # 기저사례: 집합이 빈 경우
    if len(S) == 0:
        return len(sub)

    ret = 0

    # S집합에서 선택한 수보다 큰 부분집합을 재귀
    for s in range(len(S)):
        sub.append(S[s])
        ret = max(ret, recursive_get_LIS([s for s in S[s:] if sub[-1] < s], sub))
        sub.pop()
    
    return ret

def recursive_get_LIS2(S):
    # 기저사례 S가 빈 경우
    if len(S) == 0: return 0

    ret = 0

    for i in range(len(S)):
        sub = []
        for j in range(i+1, len(S)):
            if S[i] < S[j]:
                sub.append(S[j])
        ret = max(ret, 1 + recursive_get_LIS2(sub))
    
    return ret

# print(recursive_get_LIS([3, 2, 1, 7, 5, 4, 2, 6]))
# print(recursive_get_LIS2([3, 2, 1, 7, 5, 4, 2, 6]))

# 동적계획법
cache = [-1] * 10

# start 시작 인덱스부터 부분문제의 답을 cache에 저장
def dynamic_get_LIS(S, start):
    # 기저사례: 메모이제이션
    if cache[start] != -1:
        return cache[start]

    cache[start] = 1

    for i in range(start + 1, len(S)):
        if S[start] < S[i]:
            cache[start] = max(cache[start], 1 + dynamic_get_LIS(S, i))
        
    return cache[start]

# 집합 S의 모든 인덱스를 순차적으로 탐색
def lis_helper(S):
    maxLen = 0
    for i in range(len(S)):
        maxLen = max(maxLen, dynamic_get_LIS(S, i))
    
    return maxLen

# print(lis_helper([3, 2, 1, 7, 5, 4, 2, 6]))
# print(cache)

# 위 dynamic_get_LIS 함수를 변형
# start == -1 이면 모든 인덱스를 탐색하는 방법
# 최초 start의 값이 -1이기 때문에 인덱스를 start+1로 참조
def dynamic_get_LIS2(S, start=-1):
    if start == -1:
        maxLen = 0
        for i in range(0, len(S)):
            maxLen = max(maxLen, dynamic_get_LIS2(S, i))

        return maxLen
    else:
        #기저사례: 메모이제이션
        if cache[start] != -1:
            return cache[start]

        # S[start]은 항상 존재하기 때문에 1
        cache[start] = 1

        for i in range(start, len(S)):
            if S[start] < S[i]:
                cache[start] = max(cache[start], 1 + dynamic_get_LIS2(S, i))
        
        return cache[start]

print(dynamic_get_LIS2([3, 2, 1, 7, 5, 4, 2, 6]))
print(cache)

"""
    더 빠른 해법이 존재함
    O(nlgn) 시간복잡도를 갖는 알고리즘
    텅빈 수열에서 시작해 숫자를 하나씩 추가해 나가며 각 길이를 갖는 증가 수열 중 가장 마지막 수가 작은 것이 무엇인지 추적
    ex: 
    첫 다섯 원소가 '5 6 7 1 2 ...'라는 집합 S 에서 LIS는 길이가 3인 '5 6 7'임
    반면 길이가 2인 부분 증가 수열은 '5 6' '5 7' '1 2'로 세개가 있는데 그 뒤에 수열이 계속 존재한다면 그 중 '1 2'가 가장 유리하다.
    다음에 연결해 길이가 3인 수열을 만들 수 있는데 원소를 추가하는 과정에서 아래와 같은 배열을 유지한다.

    C[i] = 지금까지 만든 부분 배열이 갖는 길이 i인 증가 부분 수열 중 최소의 마지막 값
    
    이 값을 이용해 코드를 개선하면 LIS의 길이 k에 대해 O(nk)를 가질 수 있고
    C[]가 항상 순증가한다는 사실을 기반으로 C[]를 이분검색하면 O(nlgk) <= O(nlgn)의 알고리즘을 얻을 수 있다.
"""