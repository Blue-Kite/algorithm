import sys
n, k = map(int, input().split())
a = list(map(int, input().split()))
t = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            ans = a[i]+a[j]+a[m]
            t.add(ans)
t = list(t)
t.sort(reverse=True) #리스트 역순
print(t[k-1])