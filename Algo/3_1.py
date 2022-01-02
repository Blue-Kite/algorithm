import sys
# sys.stdin=open("input.txt", "rt")
n = int(input())
for i in range(n):
    s = input()
    s = s.upper()
    wordlen = len(s)
    for k in range(wordlen//2):
        word = s[k]
        if word != s[wordlen-1-k]:
            print("#%d NO" %(i+1))
            break
    else:
        print("#%d YES" %(i+1))
