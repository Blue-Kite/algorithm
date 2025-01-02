#투포인터
def solution(people, limit):
    answer = 0
    people.sort()
    n = len(people)

    i = 0
    j = n - 1

    while i<=j:
        if people[i] + people[j] <= limit:
            answer += 1
            i += 1
            j -= 1
        else:
            answer += 1
            j -= 1


    return answer