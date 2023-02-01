#2205
#백준 1806번 부분합 
#https://www.acmicpc.net/problem/1806

#부분합이 s 이상 것중 가장 짧은 길이 출력 
#투포인터

import sys 
n, s = map(int, input().split())
nums = list(map(int, input().split()))
start = 0 #start와 end 수열 처음에서 시작함 
end = 0
answer = 0
minlen = sys.maxsize #시스템의 최대 사이즈 

# 처음에 for 구문 사용하면 i, j를 바꾸는 게 소용없음

while True:
  if answer >= s:
    answer -= nums[start] #왼쪽걸 빼줌
    minlen = min(minlen, end-start)
    start += 1
  elif end == n: #end가 수열끝이면 
    break
  else: #아직 s보다 작으면
    answer += nums[end]  #오른쪽걸 더해줌 
    end += 1
        
if minlen == sys.maxsize:
    print(0)
else:
    print(minlen)