def solution(d, budget):
    answer = 0
    total = 0
    
    for money in sorted(d):
        if total + money <= budget:
            answer += 1
            total += money
            
    return answer