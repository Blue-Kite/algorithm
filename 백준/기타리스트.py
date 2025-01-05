#곡의 개숫, 시작볼륨, 최대볼륨 1 ≤ N ≤ 50, 1 ≤ M ≤ 1,000, 0 ≤ S ≤ M 

"""
dp 형태 
        볼륨 
곡의 개수 
"""
n, s, m = map(int, input().split())
v = list(map(int, input().split()))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[0][s] = 1 #연주가능한 경우 

for k in range(1, n+1):
    #시작볼륨이 0도 가능하기 때문에 
    for i in range(0, m+1):
        prev = dp[k-1][i] #이전 스텝 모든 볼륨 
        #연주된적 있다면
        if prev != 0:
            if 0 <= i + v[k-1] <= m:
                dp[k][i+v[k-1]] = 1
            if 0<= i - v[k-1]<= m:
                dp[k][i-v[k-1]] = 1
result = -1
for i in range(m, -1, -1):
    if dp[n][i] == 1:
        result = i
        break
print(result)
            
            




