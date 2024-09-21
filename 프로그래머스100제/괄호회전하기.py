from collections import deque

def check(slist):
    couple = {')': '(', '}': '{', ']' : '['}
    stack = []
    for s in slist:
        if s not in couple:
            stack.append(s)
        else:
            if not stack:
                return False
            if stack.pop() != couple[s]:
                return False
                
    if stack:
        return False

    return True

def solution(s):
    n = len(s)
    answer = 0 
    q = deque(s)
    for i in range(n):
        q.append(q.popleft())
        if check(q):
            answer += 1
    return answer