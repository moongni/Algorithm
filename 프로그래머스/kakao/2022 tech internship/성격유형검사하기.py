INF = 10 ** 5

def solution(alp, cop, problems):
    # 목표 alp cop 구하기
    goal_alp = goal_cop = 0
    for problem in problems:
        if problem[0] > goal_alp:
            goal_alp = problem[0]
        if problem[1] > goal_cop:
            goal_cop = problem[1]
            
    DP = [[INF] * (goal_cop + 1) for _ in range(goal_alp + 1)]
    DP[alp][cop] = 0
    for i in range(alp, goal_alp + 1):
        for j in range(cop, goal_cop + 1):
            # 알고리즘 공부하는 경우
            if 0 <= i - 1:
                DP[i][j] = min(DP[i][j], DP[i - 1][j] + 1)
            # 코딩력 공부하는 경우
            if 0 <= j - 1:
                DP[i][j] = min(DP[i][j], DP[i][j - 1] + 1)
                
            # 문제를 해결하는 경우
            for problem in problems:
                before_solve_i = i - problem[2]
                before_solve_j = j - problem[3]
                if problem[0] <= before_solve_i and problem[1] <= before_solve_j:
                    DP[i][j] = min(DP[i][j], DP[before_solve_i][before_solve_j] + problem[4])
    return DP[goal_alp][goal_cop]