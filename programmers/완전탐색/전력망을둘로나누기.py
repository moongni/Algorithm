def solution(n, wires):
    answer = n
    connected = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for from_, to_ in wires:
        connected[from_][to_] = connected[to_][from_] = 1

    # 연결된 전력망의 개수를 반환
    def get_connected(from_, curr):
        temp_connected = [i for i in range(1, n+1) if connected[curr][i] == 1 and \
                          (i != from_ and i != curr)]
        # 기저사례: 말단 노드의 경우
        if not temp_connected:
            return 1

        ret = 1
        for next in temp_connected:
            ret += get_connected(curr, next)    
        
        return ret

    for from_, to_ in wires:
        connected[from_][to_] = connected[to_][from_] = 0
        answer = min(answer, abs(get_connected(from_,from_) - get_connected(to_,to_)))
        connected[from_][to_] = connected[to_][from_] = 1

    return answer

def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        print(sub)
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))

    return ans
print(solution(9,[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))