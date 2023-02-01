# 실패율 큰 -> 작음 정렬 answer 
# stages[i] = n  n번스테이지 실패

def solution(N, stages):
    answer = []
    fplayer = 0 #실패사람 
    aplayer = 0 #스테이지에 도달 인간
    players = len(stages) #유저 수 

    result = []
    for i in range(1, N+1): #1부터 n 스테이지 
        if stages.count(i): #i스테이지 실패한 인간
            fplayer = stages.count(i)
            result.append([i,fplayer / (players - aplayer)])
            aplayer += fplayer
        else:
            result.append([i, 0]) #스테이지에 통과한 사람이 없으면 실패율은 0인게 조건 

    result.sort(key=lambda x:x[1], reverse=True)

    for i in result:
        answer.append(i[0])
    return answer