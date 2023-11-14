def solution(sticker):
    n = len(sticker)
    if n <= 3:
        return max(sticker)
    
    first_sum = [0] * n
    first_sum[0] = sticker[0]
    first_sum[1] = sticker[0]
    for i in range(2, n-1):
        first_sum[i] = max(first_sum[(i-2) % n] + sticker[i], 
                           first_sum[(i-1) % n])

    second_sum = [0] * n
    second_sum[1] = sticker[1]
    second_sum[2] = sticker[1]
    for i in range(3, n):
        second_sum[i] = max(second_sum[(i-2) % n] + sticker[i],
                            second_sum[(i-1) % n])

    last_sum = [0] * n
    last_sum[0] = sticker[-1]
    last_sum[-1] = sticker[-1]
    for i in range(1, n-2):
        last_sum[i] = max(last_sum[(i - 2) % n] + sticker[i],
                         last_sum[(i - 1) % n])
    
    return max(max(first_sum), max(second_sum), max(last_sum))
