#len(딕셔너리)는 결국 키종류의 길이임

def solution(gems):
    answer = [0, 0]
    gemslen = len(gems)
    gemskind = len(set(gems)) #보석종류

    left, right = 0, 0 #투포인터
    gemsdict = {} #보석종류별로 개수를 저장

    cnt = 0
    s, e = 1, gemslen #인덱스 저장, 문제에서 gems배열 인덱스가 1부터 시작함
    minlen = gemslen #구간의 최소 길이 저장, 젤 길어봤자 gems 길이보다 작을테니 해당값으로 초기화 

    while right<gemslen:
        if gems[right] in gemsdict.keys():
            cnt = gemsdict[gems[right]] + 1
            gemsdict[gems[right]] = cnt
        else:
            gemsdict[gems[right]] = 1
        
        right += 1 #여기서 증가를 해서 gemsdict에는 right - 1까지 보석종류 

        while len(gemsdict) == gemskind:
            if right-left < minlen:
                s = left + 1 #1부터 시작하니 실제 인덱스보다 1증가 
                e = right  
                minlen = right - left 
            
            cnt =  gemsdict[gems[left]] - 1 
            if cnt  == 0:
                del gemsdict[gems[left]]
            else:
                cnt -= 1
                gemsdict[gems[left]]  = cnt
            left += 1 #left 증가하기전 보석종류 개수 처리  
    
    print(s, e)
    return answer