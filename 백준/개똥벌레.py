#x구간은 x-1과 x사이를 의미함 
#누적합 + 이분탐색
#bisect 라이브러리, bisect_left(target, value) 
#=> 정렬된target에 value가 삽입될 위치를 반환
#bisect_left([1,2,3],4)의 경우에는 return값은 3

#https://yeoooo.github.io/algorithm/BOJ3020/


import sys
from bisect import bisect_left #이진탐색 라이브러리 
n, h = map(int, sys.stdin.readline().split())
dol = []
for _ in range(n):
    dol.append(int(sys.stdin.readline()))

top, bot = [], []  #top이 위에서 자라나는 것 
for i in range(n):
    if i%2 == 0:
        bot.append(dol[i])
    else:
        top.append(dol[i])
top.sort()
bot.sort()

#1부터 h까지 컷팅을 시도해서 최소로 잘리는 것들을 찾음
cut_num = float('inf') #파괴장애물수 
cnt = 0 #구간의 수  
for cut in range(1, h+1):
    h, b = bisect_left(top, cut), bisect_left(bot, cut)