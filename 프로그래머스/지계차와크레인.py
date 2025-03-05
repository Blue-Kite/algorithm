direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def fork(storage, std):
    keep = []

    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == std:
                #한면이라도 외부와 연결되어 있다면
                for k in range(4):
                    nx = i+direction[k][0]
                    ny = j+direction[k][1]
                    #패딩이 있어서 범위 확인 불필요
                    if storage[nx][ny] == '0':
                        keep.append((i,j)) #한번에 업데이트
                        break

    for (i, j) in keep:
        storage[i][j] = "1"
        isOutside(storage, i, j)

def crane(storage, std):
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            if storage[i][j] == std:
                storage[i][j] = "1"
                isOutside(storage, i, j)

#꺼낸 박스가 외부와 연결되었다면 0으로 바꾸어줌
#중요 재귀적!!
def isOutside(storage, i, j):
    outside = False #이게 외부로 바뀌면 재귀적으로 다시 찾아야함 

    for k in range(4):
        nx = i + direction[k][0]
        ny = j + direction[k][1]

        if storage[nx][ny] == '0':
            storage[i][j] = "0"
            outside = True
            break
    
    if outside:
        for k in range(4):
            nx = i + direction[k][0]
            ny = j + direction[k][1]
            if storage[nx][ny] == "1":
                storage[nx][ny] = "0"
                isOutside(storage, nx, ny)

def solution(storage, requests):
    answer = 0
    n = len(storage[0])
    storage = [list("0"+ s + "0") for s in storage] #외부와 구별을 위해 0으로 패딩
    storage.insert(0, ["0"] * (n+2))
    storage.append(["0"] * (n+2))

    for r in requests:
        if len(r) == 1: 
            fork(storage, r)
        else:
            crane(storage, r[0])
    
    for i in range(1, len(storage)-1):
        for j in range(1, len(storage[0])-1):
            #외부와 연결 - 0, 외부와 연결x 꺼냈음 - 1
            if storage[i][j] not in ['0', '1']:
                answer += 1

    return answer