def solution(n, lost, reserve):
    new_lost = set(lost) - set(reserve)
    new_reserve = set(reserve) - set(lost)

    for need in new_lost:
        if need + 1 in new_reserve:
            new_reserve.remove(need + 1)
        elif need - 1 in new_reserve:
            new_reserve.remove(need - 1)
        else:
            n -= 1

    return n