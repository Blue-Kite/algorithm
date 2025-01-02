import heapq
n,m = map(int, input().split())#노드, 간선의 개수 
start = int(input()) #시작 노드
graph = [[] for i in range(n+1)] #[v, w]
distance = [INF for _ in range(n+1)]

def dij(start):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop()

        if distance[now] < dist:
            continue

        for v in graph[now]:
            cost = v[1] + dist 
            if cost < distance[v[0]]:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))