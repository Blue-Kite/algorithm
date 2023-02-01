n, k = map(int, input().split())
won = []
for _ in range(n):
    won.append(int(input()))
won.sort(reverse=True)

i = 0
cnt = 0
while k > 0:
    if won[i] <= k:
        cnt += k // won[i]
        k = k % won[i]

print(cnt)
