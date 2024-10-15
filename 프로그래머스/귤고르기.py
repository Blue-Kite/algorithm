#counter 정렬
#가장 많은 타입을 먼저 선택함

from collections import Counter

def solution(k, tangerine):
    answer = 0
    total = 0
    target_counter = Counter(tangerine)
    target = sorted(target_counter.items(), key=lambda x:x[1], reverse=True)

    for t in target:
        total += target_counter[t[0]]
        answer += 1
        
        if total >= k:
            return answer

  