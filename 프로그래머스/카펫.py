import math
def solution(brown, yellow):
    answer = []
    total = brown + yellow

    #가능한 모든 세로에 대해
    for v in range(3, int(math.sqrt(total)) + 1):
        h = total // v
        
        if total % v == 0 and (h+v)*2 - 4 == brown:
            answer.append(h)
            answer.append(v)
            
    return answer