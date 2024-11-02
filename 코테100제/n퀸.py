def solution(n):
    answer = 0
    queen = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if not queen[i][j]:
                queen[i][j] = 1
            
    return answer