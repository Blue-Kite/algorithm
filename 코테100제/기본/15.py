from collections import deque

#원형테이블, 순서유지 -> 큐 자료구조 
def solution(N, K):
    queue = deque(range(1, N+1))

    while len(queue) > 1: 
        for _ in range(K-1):
            queue.append(queue.popleft()) 
        queue.popleft() 
    return queue[0] 
    
    
print(solution(5,2))