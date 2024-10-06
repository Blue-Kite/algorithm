import heapq
INF = int(1e9)

def solution(N, road, K):
    graph = [[] for _ in range(N+1)]
    distance = [INF] * (N+1)

    #양방향 그래프 
    for a, b, c in road:
        graph[a].append((b, c))
        graph[b].append((a, c))

    heap = []
    heapq.heappush(heap, (0, 1)) #가중치, 노드번호
    distance[1] = 0

    while heap:
        dist, node = heapq.heappop(heap)

        #v: 이웃노드, d: 현재 노드에서 이웃노드까지 가중치   
        for v, d in graph[node]:
            cost = dist + d #새로운 경로가 
            if cost < distance[v]:
                distance[v] = cost
                heapq.heappush(heap, (cost, v))
                
    answer = [1 for d in distance if d <= K]
    return sum(answer)