def solution(n):
    answer = 0
    n = str(n)
    print(n)
    n = sorted(list(n), reverse=True)
    return int(''.join(n))