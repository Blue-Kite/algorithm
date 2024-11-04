def solution(diffs, times, limit):
    e = max(diffs) #숙련도 
    s = min(diffs)
    time = 0
    answer = e + 1

    #같거나... 작을때
    while s<=e: 
        k = (e+s) // 2
        n = len(diffs)
        time = 0 #현재 시간 
        i = 0 #현재 풀고 있는 문제의 인덱스 

        while i < n:
            if diffs[i] > k:
                time_prev = times[i-1] if i > 0 else 0
                time += (times[i] + time_prev) * (diffs[i] - k) + times[i]
            else:
                time += times[i]
            i+=1
        if time <= limit:
            e = k - 1
            answer = min(answer, k)
        else:
            s = k + 1
    return answer