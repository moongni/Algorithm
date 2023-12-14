# 현재 시간에 들어온 요청 중 가장 짧은 수행시간을 가진 일 먼저 실행
# 현재 시간에 들어온 요청이 없으며 앞으로 들어올 요청이 있으면 그시간까지 대기
def solution(jobs):
    # 요청 시간을 기준으로 정렬
    jobs.sort(key=lambda x: (x[0], x[1]))
    curr = 0
    answer = 0
    n_jobs = len(jobs)

    # 모든 작업 수 만큼 반복
    for _ in range(n_jobs):
        worklist_by_runtime = sorted([job for job in jobs if job[0] <= curr], key=lambda x: x[1])

        # 현재 시간보다 이전에 들어온 작업이 있는 경우
        # 그 중 수행시간이 제일 짧은 것 우선
        if worklist_by_runtime:
            curr_work = worklist_by_runtime[0]
            jobs.remove(curr_work)
            curr += curr_work[1]
            answer += curr - curr_work[0]
        # 현재 시간보다 이전에 들어온 작업이 없는 경우
        # 이후 가장 빠르게 들어온 요청 중 제일 짧은 것 우선
        else:
            curr_work = jobs.pop(0)
            curr = curr_work[0] + curr_work[1]
            answer += curr - curr_work[0]

    return answer // n_jobs

print(solution([[0, 3], [1, 9], [2, 6]]	))