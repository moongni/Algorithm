"""
    타일 채우기 문제
    2 x n 크기의 사각형을 2 x 1 크기의 타일로 채우는 방법의 수를 계산하는 문제
    
    n = 5 일 때 8가지 경우
    n의 최대값은 100
"""
def tiling(lo, n):
    # 기저사례
    if lo == n:
        return 1

    ret = 0

    # 세로 한줄
    ret += tiling(lo + 1, n)

    # 가로 두줄
    if lo + 1 < n:
        ret += tiling(lo + 2, n)

    return ret

# print(tiling(0, 5))

# 시간복잡도 O(n)

# print(tiling2(100))
# print(cache)

"""
    비대칭 타일 세기
    2 x n의 타일을 2 x 1 or 1 x 2 의 타일로 채우는 경우 중 좌우가 대칭이 되는 경우를 제외한 비대칭일 경우를 반환한다.
    전체 경우 중 대칭의 경우를 뺸다.
    대칭이 되는 경우
    넓이가 홀수 일 때, 가장 가운데 세로하나의 타일을 기준으로 대칭
    넓이가 짝수 일 때, 가운데 가로 두개의 타일을 기준으로 대칭 or 가운데 기준으로 대칭
"""
MOD = 1_000_000_007
def alltiling(width):
    cache = [-1] * (width + 1)

    def tiling2(width):
        if width <= 1:
            return 1

        if cache[width] != -1: return cache[width]    

        cache[width] = tiling2(width - 1) + tiling2(width - 2)

        return cache[width]    

    return tiling2(width)

def asynctiling(width):
    # 홀수일 경우
    if width % 2 == 1:
        return (alltiling(width) - alltiling(width // 2) + MOD) % MOD

    # 짝수의 경우
    ret = alltiling(width)
    # 가운데 기준으로 대칭
    ret = (ret - alltiling(width // 2) + MOD) % MOD    
    # 가운데 가로 두개의 타일이 존재
    ret = (ret - alltiling(width // 2 - 1) + MOD) % MOD
    return ret

print(asynctiling(2))
print(asynctiling(4))
print(asynctiling(92))