import sys
n = int(sys.stdin.readline())
#nums = []
table = [0 for _ in range(10001)]
for _ in range(n):
    #nums.append(sys.stdin.readline()) => 공간복잡도 문제생김
    num = int(sys.stdin.readline())
    table[num] += 1

for i in range(10001):
    if table[i] != 0:
        for _ in range(table[i]):
            print(i)