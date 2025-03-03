import math
def solution(progresses, speeds):
    answer = []
    time = [math.ceil((100 - progresses[i])/speeds[i])for i in range(len(progresses))] #각 작업이 걸리는 일 수
    cnt = 0
    std = time[0] #배포 기준점, 이거보다 작은 거는 묶어서 배포함 
    
    for t in time:
        if t <= std:
            cnt += 1
        else:
            answer.append(cnt)
            cnt = 1 
            std = t      
    
    answer.append(cnt)
    return answer