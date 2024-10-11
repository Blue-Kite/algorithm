import sys
sys.setrecursionlimit(1000000) 
input = sys.stdin.readline

n, m = map(int, input().split())
par = [i for i in range(n+1)] #각 노드의 루트 노드를 저장 

def union(a,b):
	root_a = find(a)
	root_b = find(b)

	if root_a < root_b:
		par[root_b] = root_a
	else:
		par[root_a] = root_b

def find(a):
	#본인이 루트라면 
	if par[a] == a:
		return a 
	else:
		par[a] = find(par[a]) #root 바로 밑에 a가 연결된거처럼 
		return find(par[a])

for _ in range(m):
	x, a, b = map(int, input().split())
	if x == 0:
		union(a, b)
	else:
		if find(a) == find(b):
			print('YES')
		else:
			print('NO')