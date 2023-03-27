def solution(triangle):
    len_triangle = len(triangle)
    cache = [[-1 for _ in range(len_triangle)] for _ in range(len_triangle)]

    def get_max_sum(y, x):
        # 기저사례 바닥에 도착
        if y == len_triangle or x == len(triangle[y]):
            return 0
        # 메모이제이션
        if cache[y][x] != -1:
            return cache[y][x]
        
        # 아래로 가는 경우 오른쪽 아래로 가는 경우 중 맥스 값 저장
        cache[y][x] = max(triangle[y][x] + get_max_sum(y+1, x),\
                        triangle[y][x] + get_max_sum(y+1, x+1))
        return cache[y][x]
    
    return get_max_sum(0, 0)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))

"""
테스트 1 〉	통과 (0.04ms, 10.2MB)
테스트 2 〉	통과 (0.05ms, 10.2MB)
테스트 3 〉	통과 (0.18ms, 10.2MB)
테스트 4 〉	통과 (0.63ms, 10.2MB)
테스트 5 〉	통과 (4.64ms, 10.5MB)
테스트 6 〉	통과 (0.80ms, 10.3MB)
테스트 7 〉	통과 (5.27ms, 10.5MB)
테스트 8 〉	통과 (0.63ms, 10.2MB)
테스트 9 〉	통과 (0.03ms, 10.1MB)
테스트 10 〉	통과 (0.38ms, 10.1MB)
효율성  테스트
테스트 1 〉	통과 (85.61ms, 19MB)
테스트 2 〉	통과 (68.02ms, 17.1MB)
테스트 3 〉	통과 (100.26ms, 20.5MB)
테스트 4 〉	통과 (89.23ms, 19.3MB)
테스트 5 〉	통과 (82.55ms, 18.6MB)
테스트 6 〉	통과 (108.49ms, 20.7MB)
테스트 7 〉	통과 (95.11ms, 19.8MB)
테스트 8 〉	통과 (76.83ms, 18.3MB)
테스트 9 〉	통과 (84.07ms, 18.6MB)
테스트 10 〉	통과 (97.31ms, 20.1MB)
"""