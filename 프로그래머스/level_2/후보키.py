from itertools import product

def solution(relation):
    answer = 0
    n_relation = len(relation)
    n_attrs = len(relation[0])
    cadidates = set()
    
    for i in range(n_attrs):
        for cadi in product(range(n_attrs), repeat=i):
            # 최소성 확인
            for c in cadidates:
                if len(c - cadi) == 0:
                    continue
            
            # 유일성 확인
            unique = set()
            for rel in relation:
                temp = tuple()
                for c in cadi:
                    temp += (rel[c],)
                unique.add(temp)
            
            if len(unique) == n_relation:
                answer += 1
    
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))