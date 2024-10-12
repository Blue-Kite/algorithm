def solution(n,a,b):
    answer = 0

    while a != b:
    	a = (a+1) // 2 #+1를 해야지 홀수도 다음 라운드 참가자 번호와 일치 
    	b = (b+1) // 2
    	answer += 1

    return answer