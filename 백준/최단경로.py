import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
k = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1) #k로부터 정점까지 최단경로 배열 

#그래프 정보
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

def dij(start):
    q = []
    heapq.heappush(q, (0, start))

    while q:
        dist, node = heapq.heappop(q)

        if distance[node] > dist:
            continue
        
        for i in graph[node]:
            cost = dist + i[1]
            if const < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dij(k)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INF')
    else:
        print(distance[i])