from collections import deque

def solution(board):
    answer = 0
    n = len(board)
    visited = [[0 for _ in range(n)] for _ in range(n)] #방문겸 비용 저장 
    direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    q = deque([])
    q.append([0, 0, -1, 0])

    while q:
    	x, y, d, c = q.popleft()

    	for idx, (dx, dy) in enumerate(direction):
    		nx = x + dx
    		ny = x + dy

    		if 0<=nx<n and 0<=ny<n and board[nx][ny] == 0:
    			cost = c + (100 if idx == d else 600)

    			if visited[nx][ny] == 0 and visited[nx][ny] > cost:
    				visited[nx][ny] = cost
    				q.append([nx, ny, idx, cost])

    return visited[n-1][n-1]