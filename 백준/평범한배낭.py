#220521
#백준 12865 평범한 배낭 
#https://www.acmicpc.net/problem/12865

#냅색(Knapsack) 알고리즘   https://hongcoding.tistory.com/50
n, k = map(int, input().split())
bags = []  #최대 물건 무게 합 7
for i in range(n):
    bags.append(list(map(int, input().split())))

dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

# 의문점 첫번째 물건을 가져갈것인가, 버리고 이후 물건들로 버릴것인가?
for i in range(n):
    w = bags[i][0]
    v = bags[i][1]
