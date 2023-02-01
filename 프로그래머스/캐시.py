#LRU
"""
else 부분이 이게 안되는 이유는 캐시가 0인 경우가 있음 
answer += miss
caches.append(city)
if len(caches) == cacheSize:
    caches.pop()
caches.append(city)

"""
def solution(cacheSize, cities):
    answer = 0
    hit = 1
    miss = 5
    caches = []

    for city in cities:
        #대소문자구별x
        city = city.upper()
        if city in caches:
            answer += 1
            caches.remove(city)
            caches.append(city) #삭제하고 제일 최근에 넣어줌(LRU)
        else:
            answer += miss
            caches.append(city)
            if len(caches) == cacheSize:
                caches.pop()
            caches.append(city)
        
    return answer