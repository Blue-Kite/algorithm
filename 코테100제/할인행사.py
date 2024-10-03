def solution(want, number, discount):
    answer = 0
    wdict = {}
    for i in range(len(want)):
        wdict[want[i]] = number[i]

    for j in range(len(discount)-9):
        dlist = [j:j+10]
        print(dlist)
    return answer