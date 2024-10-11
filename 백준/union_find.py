n, m = map(int, input().split())
par = [i for i in range(n+1)] #각 노드의 루트 노드를 저장 

def union(a,b):
	par[b] = a

def find(a):
	#본인이 루트라면 
	if par[a] == a:
		return a 
	else:
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


