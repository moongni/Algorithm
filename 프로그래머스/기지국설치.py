def solution(n, stations, w):
    answer = 0
    start = 1
    width = 2 * w + 1
    for station in stations:
        left = station - w
        right = station + w
        if start < left:
            ranges = (left - start)
            answer += ranges // width if ranges % width == 0 else ranges // width + 1 
        start = right + 1
    if start < n + 1:
        ranges = (n + 1 - start)
        answer += ranges // width if ranges % width == 0 else ranges // width + 1 
        
    return answer