'''
2차원 dp 
dp[a][b] : a알고력과 b코딩력을 가지기 위한 최소 시간  
와 이걸 어떻게 푸냐...
https://tech.kakao.com/posts/530
'''

def solution(alp, cop, problems):
    answer = 0  
    INF = int(2e9)

    #묹제에서 요구하는 목표 알고력, 목표 코딩력
    max_alp, max_cop = 0, 0
    for p in problems:
        max_alp = max(max_alp, p[0])
        max_cop = max(max_cop, p[1])
    
    #예외케이스 ; 목표보다 현재 가진 능력이 더 많으면
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)

    #dp 초기화
    dp = [[INF for _ in range(max_cop+1)] for _ in range(max_alp+1)]
    dp[alp][cop] = 0

    for i in range(alp, max_alp+1):
        for j in range(cop, max_cop+1):
            if i < max_alp:
                dp[i+1][j] = min(dp[i+1][j], dp[i][j] + 1)
            if j < max_cop:
                dp[i][j+1] = min(dp[i][j+1], dp[i][j] + 1)

            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                #i,j로 풀수 있는 문제라면 풀고 dp 업데이트
                if i >= alp_req and j >= cop_req:
                    alp_nxt = min(i+alp_rwd, max_alp) #풀고나서 
                    cop_nxt = min(j+cop_rwd, max_cop) 
                    dp[alp_nxt][cop_nxt] = min(dp[alp_nxt][cop_nxt] , dp[i][j] + cost)
    
    return dp[max_alp][max_cop]

