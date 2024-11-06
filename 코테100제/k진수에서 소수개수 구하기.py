def solution(n, k):
    answer = 0
    # 숫자를 k진법으로 변환: 나머지를 왼쪽에 뿥여나감 
    word=""
    while n:            
        word = str(n%k)+word
        n=n//k
        
    word=word.split("0")

    for w in word:
        #k보다 n이 작으면 0이 될수도 있음 
        if len(w)==0:    
            continue
        if int(w)<2:
            continue
        
        sosu = True
        for i in range(2,int(int(w)**0.5)+1): 
            if int(w)%i==0:
                sosu=False
                break
        if sosu:
            answer+=1
    return answer