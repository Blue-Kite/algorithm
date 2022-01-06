import sys
# sys.stdin=open("input.txt", "rt")
s = input()
ans = ""
for w in s:
    if w in ['1','2','3','4','5','6','7','8','9','0']:
        if ans == '' and  w == '0':
            continue
        ans += w
ans = int(ans)
print(ans)

cnt = 0
for i in range(1, ans+1):
    if ans %i == 0:
        cnt += 1
print(cnt)
