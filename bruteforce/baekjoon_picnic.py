"""
    백준알고리즘 2026번 소풍 문제
    원장선생님께서는 1부터 N까지 번호가 붙은 N(K ≤ N ≤ 900)명의 학생들 중에서 K(1 ≤ K ≤ 62)명의 학생들을 소풍에 보내려고 한다. 
    그런데 원장선생님께서는 중간에 싸움이 일어나면 안되므로 소풍을 갈 학생들이 모두 서로 친구 사이이기를 원한다. 
    원장선생님께서는 이러한 일을 이번에 조교로 참가한 고은이에게 친구 관계에 대한 정보를 F(1 ≤ F ≤ 5,600)개를 주시며 K명을 선발하라고 부탁하였다.

    고은 조교를 도와 소풍을 가게 될 K명의 학생들을 결정하시오.

    입력 : n k f , f개의 줄

"""

# 입력
k, n, f = map(int, input().split())
areFriends = [[ False ] * (n + 1) for _ in range(n + 1)]
n_friends = [0] * (n + 1)
taken = [False] * (n + 1)
done = False

for i in range(f):
    a, b = map(int, input().split())
    areFriends[a][b] = areFriends[b][a] = True
    n_friends[a] += 1
    n_friends[b] += 1

def baekjoon_picnic(taken):
    for i in range(1, n + 1):
        if n_friends[i] < k - 1: continue
        if done: break
        
        taken[i] = True
        dfs(i, 1)
        taken[i] = False

    if not(done):
        print(-1)

def dfs(now, depth):
    global done

    if done: return

    if depth == k:
        for i in range(len(taken)):
            if taken[i]:
                print(i)
        done = True
        return
    
    for i in range(now + 1, n + 1):
        if areFriends[now][i] and isFriend(i):
            taken[i] = True
            dfs(i, depth + 1)
            taken[i] = False

def isFriend(target):
    for i in range(1, n + 1):
        if taken[i] and not(areFriends[target][i]):
            return False
    
    return True


baekjoon_picnic(taken)