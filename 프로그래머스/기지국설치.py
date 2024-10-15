#나중에 다시 풀기 

def solution(n, stations, w):
    answer = 0
    location = 1 #아파트 탐색위치
    idx = 0 #기지국 위치 인덱스

    while location <= n:
        
        if idx < len(stations) and stations[idx] - w <= location <=  stations[idx] + w:
            location = stations[idx] + w + 1 #기지국 범위 밖으로 이동 
            idx += 1

        else:
            location += w * 2 + 1 #location 이 새로운 기지국 범위 안에 들어오도록하는 최적의 위치  
            answer += 1 #새로운 기지국 설치 

    return answer