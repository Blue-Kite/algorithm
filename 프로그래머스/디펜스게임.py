"""
n은 10억이라서 시간복잡도에 영향 없을것이고 enemy가 100만이라서
nlogn동안 풀어야함 

최대힙 => 만약 적군이 더 크다면 지나간 라운드에서 가장 큰적을 
골라서 무조건을 사용함 
"""
import heapq
import sys
def solution(n, k, enemy):
    maxheap = []
    result = 0 
    for i in range(len(enemy)):
        en = enemy[i]
        #매번 적을 힙에 집어넣음
        heapq.heappush(maxheap, -en)

        #무조건을 쓸수 있고 적보다 수가 적으면 무조건 사용
        if k>0 and n < en:
            muzogun = heapq.heappop(maxheap)
            n += (muzogun * -1)
            k -= 1
        n -= en
        if n<0:
            break
        result += 1
    return result

