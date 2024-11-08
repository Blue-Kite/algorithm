from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []

    for n in course:
        #n은 코드를 구성할 단품 메뉴 개수 
        food = []
        for o in orders:
            comb = combinations(sorted(o), n) #combination라이브러리는 문자열 순서도 고려함
            food += comb
        
        foodlist = Counter(food)
        if len(foodlist) != 0 and max(foodlist.values()) > 1:
            for m, cnt in foodlist.items():
                if cnt == max(foodlist.values()):
                    answer.append("".join(m))
        
    return sorted(answer)