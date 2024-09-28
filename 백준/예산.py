import sys
n = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))
maxmoney = int(sys.stdin.readline())
start = 1
end = max(money)
answer = 0

while start <= end:
    mid = (start + end) // 2 
    msum = 0
    for m in money:
        msum += min(m, mid)

    if msum <= maxmoney:
        answer = max(answer, mid)
        start = mid + 1
    else:
        end = mid - 1

print(answer)