"""
    소풍 문제
    n 명의 학생을 2명씩 친구끼리 짝을 지으려고 한다. 경우의 수를 구하여라
    
    입력 1. n 명의 학생, m 개의 친구 짝의 수 (n * n -1 / 2)
    입력 2. 친구인 학생 명단
"""

def picnic(friend_list, case):
    ret = 0
    
    if len(friend_list) == 0:
        return 1

    if len(case) == 0:
        return 0
    
    for i in range(0, len(case), 2):
        if case[i] in friend_list and case[i + 1] in friend_list:
            ret += picnic(list(set(friend_list) - {case[i], case[i + 1]}), case[i + 2: ])

    return ret

def picnic2(n, taken, areFriends):
    firstFree = -1

    for i in range(len(taken)):
        if not(taken[i]):
            firstFree = i
            break    
    if firstFree == -1: return 1

    ret = 0

    for i in range(firstFree + 1, n):
        if not(taken[firstFree]) and not(taken[i]) and areFriends[firstFree][i]:
            taken[i] = taken[firstFree] = True
            ret += picnic2(n, taken, areFriends)
            taken[i] = taken[firstFree] = False
    
    return ret





if __name__ == "__main__":
    # ============ picnic 1 ============
    # n = int(input())

    # for i in range(n):
    #     n_friend, n_case = map(int, input().split())

    #     case = list(map(int, input().split()))
    
    #     print(picnic(list(range(n_friend)), case))

    # ============ picnic 2 ============
    n = int(input())

    for i in range(n):
        n_friend, n_case = map(int, input().split())

        case = list(map(int, input().split()))
        
        areFriends = [[False for i in range(n_friend)] for j in range(n_friend)]
        for i in range(0, len(case), 2):
            areFriends[case[i]][case[i + 1]] = areFriends[case[i + 1]][case[i]] = True
        
        print(picnic2(n_friend, [ False for i in range(n_friend) ], areFriends))
