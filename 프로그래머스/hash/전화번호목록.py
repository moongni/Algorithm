# 0 ~ 9: [] key로 시작하는 사전 만들기
# 맨앞자리를 자른 phone_book 리스트 재귀
# 기저함수 value의 길이가 2이상이며 하나 이상이 한글자여야함
def solution(phone_book):
    # 기저사례
    if len(phone_book) <= 1: return True

    # 0 ~ 9: [] key로 시작하는 사전 만들기
    dic_by_first = {str(i): [] for i in range(10)}
    for number in phone_book:
        dic_by_first[number[0]].append(number)

    for i in range(10):
        curr_list = dic_by_first[str(i)]
        check = False

        # 길이가 하나인 글자가 있는가?
        for item in curr_list:
            if len(item) == 1:
                check = True
                break
        
        # curr_list의 길이가 2이상이며 하나 이상이 한 글자
        if len(curr_list) > 1 and check:
            return False

        if not solution([number[1:] for number in curr_list]):
            return False

    return True

def solution(phoneBook):
    phoneBook = sorted(phoneBook)
    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True

print(solution(["12","1235","123","567","88"]))