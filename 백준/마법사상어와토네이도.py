#https://www.acmicpc.net/problem/20057
#https://velog.io/@kongji47/%EB%B0%B1%EC%A4%80-20057%EB%A7%88%EB%B2%95%EC%82%AC-%EC%83%81%EC%96%B4%EC%99%80-%ED%86%A0%EB%84%A4%EC%9D%B4%EB%8F%84Python
"""
백준 풀것 
https://www.acmicpc.net/problem/10825
https://www.acmicpc.net/problem/1758
https://www.acmicpc.net/problem/10867
https://www.acmicpc.net/problem/14425
https://www.acmicpc.net/problem/11866
"""

def rotationboard(ratioboard):
    new_board = list(reversed(list(zip(*ratioboard)))) #반시계 회전 
    return new_board

n = int(input())
board = []
outsand = 0
ratioboard = [[0, 0, 0.02, 0, 0], 
	[0, 0.1, 0.07, 0.01, 0], 
    [0.05, 0, 0, 0, 0], 
    [0, 0.1, 0.07, 0.01, 0], 
    [0, 0, 0.02, 0, 0]]
p = rotationboard(ratioboard)
p1 = rotationboard(p)
p2 = rotationboard(p1)
#y는 비율 배열에서 (2,2)로 항상 고정 a는 허리케인 이동방향에 따라 달라짐. 미리 고정시키기 
a =  [(2, 1), (3, 2), (2, 3), (1, 2)]  
# 허리케인 이동방향 좌, 아래, 우, 위 
delta = [(0, -1), (1, 0), (0, 1), (-1, 0)]


for i in range(n):
    board.append(list(map(int, input().split())))
print(board)

x = startx = n // 2 
y = starty = n // 2 
thelen = 1 #태풍의 이동길이  
turn = 0 #태풍의 이동방향 1->2 / 3->0일때 그때마다 태풍의 이동길이 증가함 
movecnt = 0 #이동횟수 세는 것 
print(x, y)

#태풍의 이동 프린트
while not (x == 0 and y == 0):
    #태풍이 x, y로 이동 방향 
    dx = delta[turn][0]
    dy = delta[turn][1]
  
    x = x + dx
    y = y + dy 

    movecnt += 1
    print(x, y)
    if movecnt == thelen: #태풍의 이동길이만큼 이동하면 
        turn = (turn + 1) % 4 #방향 바꾸기 
        movecnt = 0 #이동횟수 세는 것 초기화 
        if turn == 0 or turn  == 2:
            thelen += 1

#print(outsand)
