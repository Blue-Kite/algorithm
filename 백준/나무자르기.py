import sys
n = int(sys.stdin.readline())
trees = list(map(int, sys.stdin.readline().split()))
speed = list(map(int, sys.stdin.readline().split()))

#i를 정렬 speed[i]를 기준으로 
itrees = list(range(n))
itrees = sorted(itrees, key=lambda i:speed[i])

answer = 0
for i in range(n):
    index = itrees[i]
    answer += trees[index] + i * speed[index]
print(answer) 