# 해쉬 검색
#
# 아이템들을 해쉬 리스트에 담는다. 담는 방법은 제산 방식을 사용함
# 해쉬 테이블로 만들 items, 나눌 소수 prime, 충돌 시 처리 함수 colapseFunction
# items의 요소들은 양의 정수로 가정
def hash_push_linear(items, prime):
    hash_table = [-1] * prime

    for item in items:
        hash_idx = item % prime

        # 해쉬 테이블이 충돌되는 지 검사
        if hash_table[hash_idx] == -1:            
            hash_table[hash_idx] = item
        # 해쉬 테이블 다음 인덱스를 참조하여 빈 테이블을 찾아 넣는 방법
        else:
            flag = True

            while flag:
                hash_idx += 1

                if hash_table[hash_idx] == -1:
                    hash_table[hash_idx] = item
                    flag = False
                else:
                    if hash_idx >= len(hash_table):
                        hash_idx = 0
    
    return hash_table

def hash_search_linear(hash_table, item):
    prime = len(hash_table)

    init_idx = hash_idx = item % prime

    while hash_table[hash_idx] != -1:
        if hash_table[hash_idx] == item:
            return True
        
        hash_idx += 1

        if hash_idx >= len(hash_table):
            hash_idx = 0
        
        if hash_idx == init_idx:
            break

    return False

# 체이닝
# 해쉬 테이블 충돌시 리스트에 추가
def hash_push_chaining(items, prime):
    hash_table = [[] for _ in range(prime)]

    for item in items:
        hash_idx = item % prime

        hash_table[hash_idx].append(item)

    return hash_table

def hash_search_chaining(hash_table, item):
    prime = len(hash_table)

    hash_idx = item % prime

    for i in range(len(hash_table[hash_idx])):
        if hash_table[hash_idx][i] == item:
            return True
    
    return False

lin_hash_table = hash_push_linear([2, 4, 5, 6, 22, 17, 15], 11)

print(lin_hash_table)
print(hash_search_linear(lin_hash_table, 3))
print(hash_search_linear(lin_hash_table, 22))

chain_hash_table = hash_push_chaining([2, 4, 5, 6, 22, 17, 15], 11)
print(chain_hash_table)
print(hash_search_linear(chain_hash_table, 3))
print(hash_search_linear(chain_hash_table, 22))
