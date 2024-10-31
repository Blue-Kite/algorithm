def solution(land):
    #이전 행의 최대값을 현재 행에 더해줌 
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j] += max(land[i-1][:j] + land[i-1][j+1: ])



    return max(land[len(land) - 1])