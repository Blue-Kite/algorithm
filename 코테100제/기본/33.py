def find(parents, x):
    if parents[x] == x:
        return x
    parents[x] = find(parents, x)
    return parents[x]

def union(parents, x, y):
    root_x = find(parents, x)
    root_y = find(parents, y)
    parents[root_y] = root_x
    
def solution(k, operations):
  parents = list(range(k))  
  n = k  
  
  for op in operations:  
    if op[0] == "u": 
      union(parents, op[1], op[2]) 
    elif op[0] == "f": 
      find(parents, op[1]) 

  n = len(set(find(parents, i) for i in range(k)))

  return n
  