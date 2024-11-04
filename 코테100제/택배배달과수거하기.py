#누적합 아이디어

def solution(cap, n, deliveries, pickups):
    answer = 0
    #뒷집부터 배달해야함
    del_cnt = 0
    pick_cnt = 0

    deliveries = deliveries[::-1]
    pickups = pickups[::-1]

    for i in range(n):
        del_cnt += deliveries[i]
        pick_cnt += pickups[i]

        #둘 중 하나라도 해야할게있다면
        while del_cnt > 0 or pick_cnt > 0:
            pick_cnt -= cap
            del_cnt -= cap
            answer += (n-i)*2
    return answer