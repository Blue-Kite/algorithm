from collections import deque
def bfs(tree, start, visited):
    q = deque()
    q.append(start) #start번째 노드에서 시작함
    cnt = 0 #해당 start에서 총 몇개의 노드를 방문할수 있는지
    visited[start] = True
    
    while q:
        x = q.popleft()
        cnt += 1
        for dx in tree[x]:
            if not visited[dx]:
                q.append(dx)
                visited[dx] = True
    return cnt 
    

def solution(n, wires):
    answer = n-2

    #모든 삭제 가능한 전선을 돌면서 
    for i in range(len(wires)):
        temp_wires = wires.copy() 
        temp_wires.pop(i) #i번째 value를 삭제, i번째 전선을 삭제 
        visited = [False for _ in range(n+1)] #방문 배열도 만들어서 넘김
        domain = 0
        wires_tree = [[] for _ in range(n+1)] #매번 만들어지는 그래프
    
        for w in temp_wires:
            wires_tree[w[0]].append(w[1])
            wires_tree[w[1]].append(w[0])

        for start in range(1, n+1):
            #해당 노드에서 연결된 지점이 있는 경우만
            if wires_tree[start] != []:
                domain = bfs(wires_tree, start, visited)
                break

        answer = min(answer, abs(domain - (n-domain)))
    return answer