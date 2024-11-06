from collections import deque

#sum 함수 사용하면 시간초과 걸림 
def solution(queue1, queue2):
    answer = -1
    q1 = deque(queue1)
    q2 = deque(queue2)
    cnt = 0
    q1_sum = sum(q1)
    q2_sum = sum(q2)
    #무한 반복 안되는 조건 필요 
    #합이 큰쪽 걸 하나 뽑아서 넣어줌 
    for i in range(300000):
        if q1_sum == q2_sum:
            return cnt
        elif q1_sum > q2_sum:
            n = q1.popleft()
            q2.append(n)
            q1_sum -= n
            q2_sum += n
            cnt += 1
        else:
            n = q2.popleft()
            q1.append(n)
            q1_sum += n
            q2_sum -= n
            cnt += 1
    return -1