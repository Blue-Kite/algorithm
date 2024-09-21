def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    stack.append(0) #첫 번째 인덱스로 초기화 
    
    for i in range(1, len(prices)):
        while stack and prices[stack[-1]] > prices[i]:
            j = stack.pop()
            answer[j] = i - j
        stack.append(i)
        
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j
        
    return answer