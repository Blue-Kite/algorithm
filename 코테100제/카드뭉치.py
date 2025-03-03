from collections import deque
def solution(cards1, cards2, goal):
    answer = ''
    cq1 = deque(cards1)
    cq2 = deque(cards2)
    gq = deque(goal)
    
    while gq:
        g = gq.popleft()  
        if cq1 and g == cq1[0]:
            cq1.popleft()
        elif cq2 and g == cq2[0]:
            cq2.popleft()
        else:
            return "No"
    return "Yes"