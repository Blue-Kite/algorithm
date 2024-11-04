'''
    행마다 모든 열을 검색
    조건: 해당 열에 퀸이 놓여 있는지, 2가지 대각성에 놓여 있는지 
'''
def dfs(n, cnt, col, diagonal1, diagonal2):
    answer = 0 #전체 경우 수 초기화 
    if cnt == n:
        answer += 1
    else:
        #모든 열에 대해서 
        for i in range(n):
            if col[i] or diagonal1[i+cnt] or diagonal2[i-cnt+n]:
                continue
            col[i] = diagonal1[i+cnt] = diagonal2[i-cnt+n] = True
            answer += dfs(n, cnt+1, col, diagonal1, diagonal2)
            col[i] = diagonal1[i+cnt] = diagonal2[i-cnt+n] = False
    return answer

def solution(n):
    #보드 길이, 퀸 개수=퀸을 놓은 행, 열, 대각선1, 대각선2 
    answer = dfs(n, 0, [False] * n, [False] * (n*2), [False] * (n*2))
    return answer