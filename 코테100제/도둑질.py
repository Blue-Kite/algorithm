def solution(money):
    answer = 0
    n = len(money)
    dp1 = [0 for _ in range(n)]
    dp2 = [0 for _ in range(n)]

    dp1[0] = money[0] #첫번째 집 텀 
    dp1[1] = money[0] #두번째 집도 첫번째 집을 턴게 최대값일 거임 
    dp2[0] = 0
    dp2[1] = money[1] #두번째 집 텀 

    #원형이라서 첫번째 집을 털면 마지막 집은 무조건 털면 안됨 
    for i in range(2, n-1):
        dp1[i] = max(dp1[i-1], dp1[i-2] + money[i])

    for i in range(2, n):
        dp2[i] = max(dp2[i-1], dp2[i-2] + money[i])

    return max(max(dp1), max(dp2))