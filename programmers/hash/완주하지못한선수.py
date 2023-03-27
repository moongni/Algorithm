def solution(participant, completion):
    hash = {}
    # 완주자 해시테이블 생성
    for name in completion:
        hash[name] = hash.get(name, 0) + 1
        
    for name in participant:
        if not hash.get(name):
            return name
        hash[name] -= 1

    return ""