#토핑 종류의 갯수를 동일하게함
#토핑 종류를 나눌수 있는 종류 갯수

def solution(topping):
    answer = 0
    arr1 = [0 for i in range(len(topping))] #앞에서부터 토핑의 갯수
    arr2 = [0 for i in range(len(topping))] #뒤에서부터 토핑의 갯수 
    set1 = set()
    for i in range(len(topping)):
        set1.add(topping[i])
        arr1[i] = len(set1)
    set1 = set()
    for j in range(len(topping)-1, -1, -1):
        set1.add(topping[j])
        arr2[j] = len(set1)
    
    for i in range(len(topping)-1):
        if arr1[i] == arr2[i+1]:
            answer += 1
    return answer