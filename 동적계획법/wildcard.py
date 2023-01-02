"""
    와일드 카드
    다양한 운영체제에서 파일 이름의 일부만으로 파일 이름을 지정하는 방법
    일반적인 파일명과 비슷하지만 특수 문자 * 이나 ? 포함할 수 있는 문자열

    와일드 카드 패턴을 앞에서 한 글자씩 파일명과 비교해서 모든 글자가 일치하면 대응된다고 한다.

    * : 0 글자 이상의 어떤 문자열에도 대응
    ? : 어떤 글자에도 대응
"""
# 재귀호출 완전탐색
def recursive_match(string, w):
    pos = 0

    # string[pos]와 w[pos]를 맞춰나간다.
    while pos < len(string) and pos < len(w) \
        and (w[pos] == '?' or string[pos] == w[pos]):
        pos += 1

    # 더이상 대응하지 않는다면 그 이유를 찾는다.
    # 와일드카드 끝에 도달
    if pos == len(w): 
        return pos == len(string)
    # *를 만나서 끝난 경우: *에 몇 글자를 대응해야 할지 재귀 호출로 확인
    if w[pos] == '*':
        skip = 0
        while pos + skip <= len(string):
            if recursive_match(string[pos+skip:],w[pos+1:]):
                return True
            skip += 1
    
    return False

# print(recursive_match("help", "he?p"))
# print(recursive_match("heep", "he?p"))
# print(recursive_match("helpp", "he?p"))
# print(recursive_match("help", "*p*"))
# print(recursive_match("papa", "*p*"))
# print(recursive_match("hello", "*p*"))

# 메모이제이션
cache = [[-1 for _ in range(15)] for _ in range(15)]
S = 'vidsoepeovsi'
W = "*p*"

# s, w 는 각각 S의 위치 W의 위치 정수
def dynamic_match(s, w):
    if cache[s][w] != -1:
        return cache[s][w]
    
    # S[s] 와 W[w]를 맞춰나간다.
    while s < len(S) and w < len(W) \
        and (W[w] == '?' or S[s] == W[w]):
        s += 1
        w += 1

    # 더 이상 매치가 안되는 경우 이유를 찾아야함
    # W의 끝에 도달
    if w == len(W):
        cache[s][w] = s == len(S)
        return cache[s][w]

    # '*'을 만난 경우
    if W[w] == '*':
        skip = 0
        while s + skip <= len(S):
            if dynamic_match(s + skip, w + 1):
                cache[s][w] = 1
                return cache[s][w]
            skip += 1

    cache[s][w] = 0
    
    return cache[s][w]

# print(dynamic_match(0, 0))

def print_board(board):
    for row in board:
        for col in row:
            if col < 0:
                print(f"{col} ", end='')
            else:
                print(f" {col} ", end='')
        print()

# print_board(cache)

# 분해방식을 변화시켜 시간복잡도를 줄이는 방식
# 반복문을 제거해서 O(n^2) 까지
def dynamic_match2(s, w):
    # 기저조건: 이미 수행되었던 결과
    if cache[s][w] != -1:
        return cache[s][w]

    # 글자를 매치
    if s < len(S) and w < len(W) \
        and (W[w] == '?' or S[s] == W[w]):
        cache[s][w] = dynamic_match2(s + 1, w + 1)
        return cache[s][w]

    # 더이상 매치할 수 없으면 이유를 찾는다.
    # 와일드카드의 끝인 경우    
    if w == len(W):
        cache[s][w] = s == len(S)
        return cache[s][w]
    
    # 와일드카드가 *인 경우 다음 글자가 나올 때 까지 매치
    if W[w] == '*':
        if dynamic_match2(s, w + 1) or (s <= len(S) and dynamic_match2(s + 1, w)):
            cache[s][w] = 1
            return cache[s][w]
    
    cache[s][w] = 0

    return cache[s][w]

print(dynamic_match2(0, 0))