t = int(input())

dp = [1 for _ in range(10001)] #뭐든 1로 구성할 수 있음

for i in range(2, 10001):
	dp[i] += dp[i-2]

for i in range(3, 10001):
	dp[i] += dp[i-3]

for _ in range(t):
	print(dp[int(input())])


"""
	1 : 1
	2 : 1+1, 2
	3 : 1+1+1, 1+2, 3
	4 : 1+1+1+1, 1+1+2, 2+2, 1+3

""""

