n, k = map(int, input().split())
result = []

for i in range(1, n+1, 1):
    if n % i == 0:
        result.append(i)
    if len(result) == k:
        break
        
if len(result ) == k:
    print(result[-1])
else:
    print(0)


