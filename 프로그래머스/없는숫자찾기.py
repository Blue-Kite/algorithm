def solution(numbers):
    number = [0,1,2,3,4,5,6,7,8,9]
    answer = 0

    for num in number:
        if num not in numbers:
            answer += num
    return answer