def solution(prices):
    answer = []
    answer = [0 for i in range(len(prices))]
    for i in range(len(prices)-1):
        count = 0
        for j in range(i+1, len(prices)):
            count += 1
            if prices[i] > prices[j]:
                break
        answer[i] = count
    return answer