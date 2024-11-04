def make_days(year, month, day):
    return year * 28 * 12 + month * 28 + day

def solution(today, terms, privacies):
    answer = []
    terms_dict = {}
    for t in terms:
        k, v = t.split()
        terms_dict[k] = int(v)
        
    t_year, t_month, t_day = map(int, today.split('.'))
    today_days = make_days(t_year, t_month, t_day)
    
    for i in range(len(privacies)):
        p_date, p_type = privacies[i].split()
        add_month = terms_dict[p_type]
        year, month, day = map(int, p_date.split('.'))
        p_date = make_days(year, month+add_month, day)
        
        if today_days >= p_date:
            answer.append(i+1)
        
        
    return answer