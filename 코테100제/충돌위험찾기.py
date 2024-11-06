#각 로봇들의 시간별 경로 
from collections import Counter
def solution(points, routes):
    answer = 0
    n = len(routes) #로봇수
    path = [[] for _ in range(n)] #path[i][j] 는 i번째 로봇의 j때 로봇 위치 
    
    for i in range(n):
        for j in range(len(routes[i]) - 1):
            #지금 경로와, 그 다음 경로
            start_x, start_y = points[routes[i][j] - 1]
            end_x, end_y = points[routes[i][j+1] - 1]

            total_x, total_y = abs(end_x - start_x) , abs(end_y - start_y)
            
            #맨 처음 로봇의 위치 
            if j == 0:
                path[i].append((start_x, start_y))
            
            k = total_x + total_y #음수일때를 조심하자 
            while k > 0:
                if end_x - start_x > 0:
                    path[i].append((start_x + 1, start_y))
                    start_x += 1
                    total_x -= 1
                elif end_x - start_x < 0:
                    path[i].append((start_x - 1, start_y))
                    start_x -= 1
                    total_x += 1
                else:
                    if end_y - start_y > 0:
                        path[i].append((start_x, start_y + 1))
                        start_y += 1
                        total_y -= 1
                    if end_y - start_y < 0:
                        path[i].append((start_x, start_y - 1)) 
                        start_y -= 1
                        total_y += 1
                        
                total_x, total_y = abs(end_x - start_x) , abs(end_y - start_y)
                k = total_x + total_y
    print(path)
    max_path = max(list(map(len, path)))
    #시간마다 
    for t in range(max_path):
        time_pos = [] #시간마다 위치 
        #로봇마다 
        for i in range(n):
            if t <= len(path[i]) - 1:
                time_pos.append(tuple(path[i][t]))
        cnt_time_pos = Counter(time_pos)
        for cnt in cnt_time_pos.values():
            if cnt >= 2:
                answer+= 1

    return answer
