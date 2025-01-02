'''
    행마다 모든 열을 검색
    조건: 해당 열에 퀸이 놓여 있는지, 2가지 대각성에 놓여 있는지 
'''
def dfs(queen, n, row):
    count = 0 #전체 경우 수 초기화 
    if row = n:
        return 1
    else:
        #각 행마다 
        #모든 열에 대해서 퀸을 둬서 겹치는지 확인
        for col in range(n):
            queen[row] = col

            for x in range(row):
                # 세로로 겹침
                if queen[x] == queen[row]: 
                    break
                
                # 대각선 겹침
                if abs(queen[x]-queen[row]) == (row-x):
                    break
        #반복문이 끝까지 실행된 경우만 
        else:
            count += dfs(queen, n, row+1) #다음 row
        
    return count

def solution(n):
    queen = [0]*n
    return dfs(queen, n, 0) #i번째 row의 col 인덱스 , 보드크기 , 현재 row 