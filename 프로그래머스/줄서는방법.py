#총경우수 n!
#https://dev-dain.tistory.com/205
#순열쓰면 시간복잡도 탈락 


import math 
def solution(n, k):
    answer = []
    numlist = [i for i in range(1, n+1)] 
    k -= 1 # k를 인덱스로 사용하기 위해서

    max_num = math.factorial(n) #시간복잡도는 O(n)이라고 함

    return answer