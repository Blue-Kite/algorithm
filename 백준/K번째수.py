import sys
n = int(sys.stdin.readline())
straw = []

for  _ in range(n):
  straw.append(int(sys.stdin.readline()))

straw.sort(reverse=True)
answer = -1
print(straw)

for i in range(0,n-2,1):
  if straw[i] < straw[i+1] + straw[i+2]:
    answer = straw[i+2] + straw[i] + straw[i+1]
    break
print(answer)

