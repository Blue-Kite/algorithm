#꼭 다시 풀어보기 
def solution(enroll, referral, seller, amount):
    answer = []
    boss = dict(zip(enroll, referral)) # {직원: 상사} 
    total = {name: 0 for name in enroll} # {직원 : 번돈 }
    
    for i in range(len(seller)):
        money = amount[i] * 100 #총 번 돈 
        cur_name = seller[i]
        
        while money > 0 and cur_name != '-':
            total[cur_name] += money - (money // 10)
            cur_name = boss[cur_name]
            money = money // 10
            
    return [total[name] for name in enroll]