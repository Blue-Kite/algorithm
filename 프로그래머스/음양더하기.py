#참고할 풀이 https://programmers.co.kr/learn/courses/30/lessons/76501/solution_groups?language=python3

def solution(absolutes, signs):
    answer = 0
    n = len(absolutes)
    for i in range(n):
        if signs[i]:
            absolutes[i] = 0 - absolutes[i]
            answer += absolutes[i]
        else:
            answer += absolutes[i]
    return answer