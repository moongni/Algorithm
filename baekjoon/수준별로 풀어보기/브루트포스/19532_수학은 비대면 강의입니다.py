def solution(a, b, c, d, e, f):
    assert a >= -999 and a <= 999
    assert b >= -999 and b <= 999
    assert c >= -999 and c <= 999
    assert d >= -999 and d <= 999
    assert e >= -999 and e <= 999
    assert f >= -999 and f <= 999
    
    x = -999
    while x <= 999:
        y = -999
        while y <= 999:
            if a * x + b * y == c and d * x + e * y == f:
                return x, y
            y += 1
        x += 1
    return None, None

a, b, c, d, e, f = map(int, input().split())
x, y = solution(a, b, c, d, e, f)
print(x, y) 
