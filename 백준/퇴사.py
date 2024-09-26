import sys
N = int(sys.stdin.readline())
answer = 0
plan = []
for _ in range(N):
    plan.append(list(map(int,sys.stdin.readline().split())))

def rec(day, money):
  global answer
  if day >= N:
    return
  if answer < money:
    answer = money
  rec(day+plan[day][0], money+plan[day][1])
  rec(day+1, money)

rec(0, 0)
print(answer)