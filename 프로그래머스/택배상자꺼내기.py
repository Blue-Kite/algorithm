def solution(n, w, num):
    answer = 0
    h = n//w + 1 #일부만 채워진거까지 포함한 한 층 추가
    b = 1 #상자 번호
    storages = []

    for i in range(h):
        storage = []
        for j in range(w):
            if b <= n:
                storage.append(b)
                b+=1
            else:
                storage.append(0)
        
        if i % 2 == 0:
            storages.append(storage)
        else:
            storage.reverse()
            storages.append(storage)
    
    for i in range(h):
        for j in range(w):
            if storages[i][j] == num:
                d = i
                while d < h and storages[d][j] != 0:
                    answer += 1
                    d += 1

    return answer