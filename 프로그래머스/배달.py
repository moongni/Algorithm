from collections import defaultdict, deque

def bfs(graph, N):
    queue = deque([[0, 1]])
    
    dist = [float('inf')] * (N + 1) # 계산하기 편하게 N+1 길이만큼 리스트 생성
    dist[1] = 0 # 1번 마을은 무조건 거리가 0
    
    while queue:
        current_cost, current = queue.popleft() # 현재 선택된 노드와 비용
        connected = graph[current]
        for cost, dest in connected:
            next_cost = cost + current_cost
            if next_cost < dist[dest]:
                dist[dest] = next_cost
                queue.append([next_cost, dest])
                
    return dist

def solution(N, road, K):
    graph = defaultdict(list)
    for src, dest, cost in road:
        graph[src].append([cost, dest])
        graph[dest].append([cost, src])
    dist = bfs(graph, N)
    return len([x for x in dist if x <= K]) # list comprehension

