"""
    울타리 잘라내기

    N개의 너비가 다른 울타리 중 가장 넓은 직사각형으로 잘라냈을 때의 넓이를 구하여라
    비스듬이 잘라낼 수 없다.

    내 생각 풀이
    가장 넓은 직사각형의 경우의 수
    1. 가운데를 포함
    2. 절반 중 왼쪽에 포함
    3. 절반 중 오른쪽에 포함
"""
MIN = -99999

def fence1(fences, left, right):
    # 기저사례
    if left >= right: return fences[left]

    half = (left + right) // 2

    # 왼쪽 또는 오른쪽 최대넓이 경우
    ret  = max(fence1(fences, left, half), fence1(fences, half + 1, right))

    lo = hi = half

    height = fences[half]

    # 가운데를 포함하는 경우
    # 왼쪽 오른쪽 중 더 높은 펜스로 확장
    while left < lo or hi < right:
        if hi < right and (lo == left or fences[lo - 1] < fences[hi + 1]):
            hi += 1
            height = min(height, fences[hi])
        else:
            lo -= 1
            height = min(height, fences[lo])

        ret = max(ret, (hi - lo + 1) * height)

    return ret

print(fence1([7,1,5,9,6,7,3], 0, 6))