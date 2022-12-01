"""
    외판원 문제 - 완전 탐색
    서로 연결된 n개의 도시에서 가장 적은 가중치를 가진 path를 찾는 문제

    재귀함수를 통해 모든 경우의 수를 찾음
"""
N = 5
DISTANCE = [
    [0, 2, 2, 1, 4],
    [2, 0, 3, 2, 3],
    [2, 3, 0, 2, 2],
    [1, 2, 2, 0, 4],
    [4, 3, 2, 4, 0]
]

# 가장 짧은 path를 반환하는 함수
def shortest_path(path, visited, currentLength):
    # 기저함수 : 모든 도시를 방문한 경우
    if len(path) == N:
        return currentLength + DISTANCE[path[-1]][path[0]]

    ret = float("inf")

    # 순차적으로 모든 도시 탐방
    for next in range(N):
        # 이미 방문한 도시인 경우
        if visited[next]: continue
        
        here = next
        if len(path) != 0:
            here = path[-1]

        visited[next] = True
        path.append(next)

        ret = min(shortest_path(path, visited, currentLength + DISTANCE[here][next]), ret)

        visited[next] = False
        path.pop()        
    
    return ret

path = []

print(shortest_path(path, [False] * N, 0))