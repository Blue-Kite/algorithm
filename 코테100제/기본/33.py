def find(parents, x):

def union(parents, x, y):

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
  