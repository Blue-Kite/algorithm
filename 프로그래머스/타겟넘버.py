# 연산자 자리에는 +나 -나 들어갈수 있으니 2의 n승이라고 생각함

from collections import deque
def solution(numbers, target):
    answer = 0
    n = len(numbers)
    q = deque([])
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])

    while q:
        num, idx = q.popleft()
        idx += 1
        if idx < n:
            q.append([num + numbers[idx], idx])
            q.append([num - numbers[idx], idx])
        
        if idx == n:
            if num == target:
                answer += 1      
    return answer