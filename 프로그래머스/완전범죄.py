#모든 물건 훔치기
#a의 흔적 최소화 => b가 최대한 훔치기
#2차원 dp

def solution(info, n, m):
    MAX = 120 #최대로 남길 수 있는 흔적

    # dp[a][b] : A의 누적 흔적이 a, B의 누적 흔적이 b인 상태가 가능한지
    dp = [[False for _ in range(MAX)] for _ in range(MAX)]
    dp[0][0] = True
    item_cnt = len(info)

    #아이템 갯수만큼 돌면서 A,B중 누가 선택할지
    for i in range(item_cnt):
        #각 아이템 스텝마다 독립적으로 반영하기 위해
        next_dp = [[False for _ in range(120)] for _ in range(120)]
        a_trace = info[i][0]
        b_trace = info[i][1]

        #해당 아이템에서 가능한 A,B 상태를 반영
        for a in range(n):
            for b in range(m):
                if not dp[a][b]:
                    continue
                
                if a + a_trace < n:
                    next_dp[a + a_trace][b] = True
                if b + b_trace < m:
                    next_dp[a][b + b_trace] = True

        #모든 아이템에 대해 A나 B 중 적어도 하나가 훔칠 수 없다면, 모든 dp[a][b]가 False가 반영
        for a in range(n):
            for b in range(m):
                dp[a][b] = next_dp[a][b]
        
    # 결과 찾기
    for a in range(n):
        for b in range(m):
            if dp[a][b]:
                return a
    
    return -1