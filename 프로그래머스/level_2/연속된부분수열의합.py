# 이분탐색을 활용해 연산의 수를 감소시킴
# O(nlog(n))
def solution(sequence, k):
    s_len = len(sequence)
    answer = []
    partsum = [0] * (s_len + 1)
    partsum[1] = sequence[0]
    for i in range(2, s_len + 1):
        partsum[i] = partsum[i - 1] + sequence[i - 1]

    for i in range(1, s_len + 1):
        if partsum[i] < k:
            continue
        left, right = 0, i
        while left <= right:
            mid = (left + right) // 2
            
            diff = partsum[i] - partsum[mid]
            if diff < k:
                right = mid - 1
            elif diff > k:
                left = mid + 1
            else:
                answer.append([mid, i - 1])
                break
    
    return sorted(answer, key=lambda x: (x[1] - x[0], x[0]))[0]