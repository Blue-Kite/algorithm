
def solution(n):
    answer = []
    def back(sum, selected, start):
        if sum == n:
            answer.append(selected)
        else:
            for i in range(start, n+1):
                back(sum + i, selected + [i], start)
                
    back(0, selected, 1)
    return answer

print(solution(5))