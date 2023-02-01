#종료 시간 , 시작시간으로 정렬 

n = int(input())
meetings = []
for _ in range(n):
    s, e = map(int, input().split())
    meetings.append((s, e))

meetings.sort(key=lambda x: (x[1], x[0]))

cnt, last_end = 0, 0
for start, end in meetings:
    if start >= last_end:
        cnt += 1
        last_end = end

print(cnt)