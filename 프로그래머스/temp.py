def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    numbers.sort(key = lambda x: x*3, reverse=True)
    answer = ''.join(numbers)

    #유일한 예외
    if answer == '0' * len(numbers):
        return '0'
    return answer