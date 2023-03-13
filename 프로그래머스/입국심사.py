#시간복잡도상 심사관을 기준으로 0(nlogn)까지 가능함 
#파라메트릭 서치 문제 -> 답을 정하고 조건에 맞는지 확인함 최적해를 빠르게 구하는 문제 
#대신 특정 값이 가능하면 그이하(이상) 항상 불가능하고 그이상(이하) 항상 가능한 상황이어야함 
def solution(n, times):
    answer = 999999999999999
    times.sort()
    
    start = 1
    end = n * times[len(times)-1]
    temp = 0
    
    while start<=end:
        mid = (start+end) // 2
        temp = 0 #임시 사람 수 
        for i in range(len(times)):
            temp += mid // times[i]
        if temp >= n:
            answer = min(answer, mid)
            end = mid - 1
        else:
            start = mid + 1
        
    return answer