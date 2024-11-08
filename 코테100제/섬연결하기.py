#유니온 파인드
#다시 풀어보기 

def find(par, i):
    if par[i] == i:
        return i
    else:
        par[i] = find(par, par[i])
        return par[i]
    
def union(par, rank, a, b):
    a_root = find(par, a)
    b_root = find(par, b)

    #랭크가 큰거에 연결, 덜 깊어지도록 
    if rank[a] < rank[b]:
        par[a] = b_root
    elif rank[a] > rank[b]:
        par[b] = a_root
    else:
        par[b] = a_root
        rank[a] += 1

def solution(n, costs):
    answer = 0
    cost = costs.sort(key = lambda x: x[2]) #비용 순대로 간선 정렬 
    par = [i for i in range(n+1)] 
    rank = [0 for _ in range(n+1)]
    edges = 0

    for e in costs:
        #사이클인지 확인 
        if edges == n-1:
            break

        a = find(par, e[0])
        b = find(par, e[1])

        #사이클인지 확인
        if a!=b:
            union(par, rank, a, b)
            answer += e[2]
            edges += 1

    return answer