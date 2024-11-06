# 시침 12시간에 360도 -> 1시간에 30도 -> 1초에 30도/3600 (1/120도)
# 분침 60분에 360도 -> 1초에 360도/3600 (0.1도)
# 초침 60초에 360도 -> 1초에 6도

def make_s(hour, minute, second):
    return second + minute * 60 + hour*3600

def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    second1 = make_s(h1, m1, s1)
    second2 = make_s(h2, m2, s2)

    #빼먹지 말기 
    if second1 == 0 or second1 == 12*3600:
        answer += 1

    hcount, mcount = 0, 0

    for t in range(second1, second2):
        #해당 초일때 시침, 분침, 초침의 각도는
        #360도마다 제자리이니까 
        s = (t * 6) % 360 
        m = (t / 10) % 360
        h = (t / 120) % 360

        s1 = 360 if ((t+1) * 6) % 360 == 0 else ((t+1) * 6) % 360 
        m1 = 360 if ((t+1) /10) % 360 == 0 else ((t+1) / 10) % 360 
        h1 = 360 if ((t+1) / 120) % 360 == 0 else ((t+1) / 120) % 360  

        #초침이 더 컸는데 분침이나 시침이 추월할 수는 없음 
        if s < h and s1 >= h1:
            hcount+=1
        if s < m and s1 >= m1:
            mcount+=1
        if s1 == m1 == h1:
            answer -= 1

    answer += (hcount + mcount)
    return answer