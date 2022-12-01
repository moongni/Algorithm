# 입력받은 컨테이너를 순차적으로 검색하여 item이 있으면 인덱스 리턴

def linear_search(container, item):
    for i in range(len(container)):
        if container[i] == item:
            return i
    
    return -1