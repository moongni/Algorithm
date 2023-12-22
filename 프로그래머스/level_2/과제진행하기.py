def solution(plans):
    answer = []
    stopped = []    # store stopped works
    # tuning representation of plans
    for i in range(len(plans)):
        start = plans[i][1].split(':')
        start_time = int(start[0]) * 60 + int(start[1])
        plans[i][1] = start_time
        plans[i][2] = int(plans[i][2])
    plans.sort(key=lambda x: x[1], reverse=True)

    prev_work = plans.pop()
    end_time = prev_work[1] + prev_work[2]
    while plans:
        cur_work = plans.pop()
        # finish before starting next work
        if end_time <= cur_work[1]:
            answer.append(prev_work[0])
            # doing recent stopped work
            rest_time = cur_work[1] - end_time
            while stopped and rest_time > 0:
                if stopped[-1][2] <= rest_time:
                    rest_time -= stopped[-1][2]
                    answer.append(stopped.pop()[0])
                else:
                    stopped[-1][2] -= rest_time
                    rest_time = 0
            prev_work = cur_work
            end_time = prev_work[1] + prev_work[2]
        else:
            # interupt
            prev_work[2] = (end_time - cur_work[1])
            stopped.append(prev_work)
            prev_work = cur_work
            end_time = prev_work[1] + prev_work[2]
        
    answer.append(prev_work[0])
    while stopped:
        answer.append(stopped.pop()[0])
        
    return answer