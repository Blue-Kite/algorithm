import sys
n, m = map(int, sys.stdin.readline().split())
times = []
for _ in range(n):
    times.append(int(sys.stdin.readline()))
answer = 0
#시간을 기준
#특정 시간에 n명을 할 수 있는가?
# right는 가장 비효율적으로 심사했을 때 걸리는 시간
# right는 가장 긴 심사시간이 소요되는 심사관에게 n 명 모두 심사받는 경우
left, right = 1, max(times) * m
while left <= right:
     # 모든 심사관을 거치지 않아도 mid분 동안 n명 이상의 심사를 할 수 있다면 반복문을 나감.
    mid = (left + right)//2
    people = 0
    for time in times:
        people += mid // time
        if people>=m:
            break

    #심사한 사람이 심사해야하는 n보다 많거나 같으면 right를 줄임
    #그때의 시간이 정답이 될수 있음
    if people >= m:
        answer = mid
        right = mid - 1
    else:
        left = mid + 1
    #심사한 사람이 심사해야하는 n보다 적으면 left를 늘림 
print(answer)
