from collections import Counter

def solution(topping):
    answer = 0
    topping_counter = Counter(topping) #동생이 다 먹는다 치고 
    brother = set()

    for t in topping:
        topping_counter[t] -= 1
        brother.add(t)

        if topping_counter[t] == 0:
            topping_counter.pop(t)
            
        if len(topping_counter) == len(brother):
            answer += 1

    return answer