"""
    폴리오미노
    정사각형의 변들을 서로 완전하게 붙여 만든 도형들을 폴리오미노라고 부른다.
    n개의 정사각형으로 구성된 폴리오미노들을 만드려고한다. 이 중 세로로 단조인 폴리오미노의 수가 몇개인지 반환하는 함수를 작성하라.

    1 <= n <= 100
    
    solve(n, first)
    n개의 정사각형과 첫줄에 위치할 사각형의 개수를 입력받는다.
    두번째 줄에는 n-first개의 정사각형이 1 <= second <= n-first 개 들어갈 수 있다.
    하여 모든 폴리오미노는 solve(n, first) + solve(n - first, 1) + solve(n - first, 2) ,,, solve(n -first, second)
    
"""
from printBoard import print_board

cache = [[-1 for _ in range(101)] for _ in range(101)]

def solve(n, first=0):
    # 기저조건: n == first
    if n == first:
        return 1
    
    # 메모이제이션
    if cache[n][first] != -1:
        return cache[n][first]
    
    cache[n][first] = 0

    # 초기 실행 헬퍼
    if first == 0:
        ret = 0
        for i in range(1, n + 1):
            ret += solve(n, i)
        
        return ret

    else:
        # 두번째 줄 계산
        for second in range(1, n - first + 1):
            add = second + first - 1
            add *= solve(n - first, second)
            cache[n][first] += add
    
    return cache[n][first]

def initCache(cache):
    for i in range(len(cache)):
        for j in range(len(cache[0])):
            cache[i][j] = -1

initCache(cache)
print(solve(2))
# print_board(cache)

initCache(cache)
print(solve(4))
# print_board(cache)

initCache(cache)
print(solve(92))
# print_board(cache)