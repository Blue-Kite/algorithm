#탐욕법 => 태울수 있는게 가장 좋으니
def solution(people, limit):
    answer = 0
    people.sort()
    left = 0
    i = len(people) - 1

    while left < i:
        if people[i] + people[left] <= limit:
            left += 1
            answer += 1
            i -= 1
        else:
            i -= 1
            answer += 1

    return answer