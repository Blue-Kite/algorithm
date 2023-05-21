#연결이 1 
#computer[i][i]는 항상 1

def dfs(n, graph, i, visited):
	visited[i] = True #방문처리 
	
	for j in range(n):  #방문한 노드의 이웃 중에 
		if graph[i][j] == 1 and not visited[j]: #방문한 적 있는게 없으면 
			dfs(n, graph, j, visited)

def solution(n, computers):
    answer = 0
    visited = [0] * n
      
    for i in range(n):
	    if visited[i] == 0:
		    dfs(n, computers, i, visited)
		    answer += 1
		    
    return answer