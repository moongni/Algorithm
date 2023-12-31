from collections import deque

def solution(queue1, queue2):
    sum1 = sum(queue1)
    sum2 = sum(queue2)
    q1_idx = 0
    q2_idx = 0
    tot_len = len(queue1) + len(queue2)
    answer = 0
    
    if (sum1 + sum2) % 2 == 1:
        return -1
        
    while sum1 != sum2:
        if q1_idx >= tot_len or q2_idx >= tot_len:
            return -1
        
        if sum1 > sum2:
            sum1 -= queue1[q1_idx]
            sum2 += queue1[q1_idx]
            queue2.append(queue1[q1_idx])
            q1_idx += 1
        else:
            sum1 += queue2[q2_idx]
            sum2 -= queue2[q2_idx]
            queue1.append(queue2[q2_idx])
            q2_idx += 1
        answer += 1
    return answer