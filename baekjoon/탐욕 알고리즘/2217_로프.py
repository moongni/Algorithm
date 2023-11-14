def solution(ropes):
    ropes.sort()

    n = len(ropes)
    weight = 0
    # 순회하며 가장 높은 무게를 들 수 있는 시작 로프 찾기
    for i, rope in enumerate(ropes):
        weight = max(weight, rope * (n - i))

    return weight
    
n = int(input())
ropes = [int(input()) for _ in range(n)]
result = solution(ropes)
print(result)