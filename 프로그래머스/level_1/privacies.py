# "yyyy.mm.dd" 를 day로 변환
def date_to_days(date):
    year, month, day = map(int, date.split('.'))
    return (year * 12 + month) * 28 + day

def solution(today, terms, privacies):
    # 약관 메타 데이터
    meta_ = {term[0]: int(term[1]) * 28 for term in map(str.split, terms)}
    today = date_to_days(today)

    answer = []
    
    for i in range(len(privacies)):
        date, valid_type = privacies[i].split(" ")

        valid_day = date_to_days(date) + meta_[valid_type] - 1

        # 만료기간이 지난 경우 append
        if valid_day < today:
            answer.append(i + 1)

    return answer