def solution(money):
    dp1 = [0] * len(money)
    dp1[0] = money[0]
    dp1[1] = max(money[0], money[1])

    for i in range(2, len(money) - 1):
        dp1[i] = max(dp1[i-1], money[i] + dp1[i-2])
    
    dp2 = [0] * len(money)
    dp2[1] = money[1]

    for i in range(2, len(money)):
        dp2[i] = max(dp2[i-1], money[i] + dp2[i-2])
    
    return max(dp1[-2], dp2[-1])

print(solution([1,100,1,1,100,1]))
print(solution([1,2,4,1]))