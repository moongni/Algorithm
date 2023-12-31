INF = 10 ** 5

def solution(alp, cop, problems):
    # 목표 alp cop 구하기
    goal_alp = alp
    goal_cop = cop
    for problem in problems:
        if goal_alp < problem[0]:
            goal_alp = problem[0]
        if goal_cop < problem[1]:
            goal_cop = problem[1]
            
    DP = [[INF] * (goal_cop + 1) for _ in range(goal_alp + 1)]
    DP[alp][cop] = 0
    for i in range(alp, goal_alp + 1):
        for j in range(cop, goal_cop + 1):
            # 알고리즘 공부하는 경우
            if i < goal_alp:
                DP[i + 1][j] = min(DP[i + 1][j], DP[i][j] + 1)
            # 코딩력 공부하는 경우
            if j < goal_cop:
                DP[i][j + 1] = min(DP[i][j + 1], DP[i][j] + 1)
                
            # 문제를 해결하는 경우
            for problem in problems:
                if problem[0] <= i and problem[1] <= j:
                    after_i = i + problem[2]
                    after_j = j + problem[3]
                    DP[min(goal_alp, after_i)][min(goal_cop, after_j)] = min(
                        DP[min(goal_alp, after_i)][min(goal_cop, after_j)],
                        DP[i][j] + problem[4]
                    )
                
    return DP[goal_alp][goal_cop]