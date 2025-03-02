
def convertTime(n): # 반드시 분 단위로 변환
    h = n // 100
    m = n % 100
    return h * 60 + m

def solution(schedules, timelogs, startday):
    answer = 0
    n = len(schedules)
    
    for i in range(n):
        s = startday
        for t in timelogs[i]:
            if s in [6,7]:
                s += 1
                if s == 8:
                    s = 1
                continue
            if convertTime(t) > convertTime(schedules[i])+10:
                break
            else:
                s += 1
        else:
            answer += 1

            
    return answer