n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1 = p2 = 0
ans = []

while p1 != n and p2 != m:
    if a[p1] <= b[p2]:
        ans.append(a[p1])
        p1 += 1
    else:
        ans.append(b[p2])
        p2 += 1

if p1 != n:
    for i in range(p1, n, 1):
        ans.append(a[i])
if p2 != m:
    for i in range(p2, m, 1):
        ans.append(b[i])

for x in ans:
    print(x, end=" ")
