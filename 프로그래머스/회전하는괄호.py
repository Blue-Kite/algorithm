from collections import deque

def check(slist):
    result = True
    couple = {')': '(', '}': '{', ']' : '['}
    stack = deque([])

    for s in slist:
        if s in couple.values():
            stack.appendleft(s)
        else:
            if not stack:
                return False
            else:
                s_cp = stack.popleft()
                if s_cp != couple[s]:
                    return False
    if stack:
        return False
    return result 

def solution(s):
    n = len(s)
    answer = 0 
    q = deque(s)
  
    for i in range(n):
        q.append(q.popleft())
        if check(q):
            answer += 1
    return answer