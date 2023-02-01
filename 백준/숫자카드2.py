#해시와 counter 라이브러리를 사용한 방법도 알아두기
#https://chancoding.tistory.com/45

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index 
    
n = int(input())
card = list(map(int, input().split()))
card.sort()
m = int(input())
mcard = list(map(int, input().split()))
answer = []

for mc in mcard:
    a = count_by_range(card, mc, mc)
    answer.append(a)
print(' '.join(map(str, answer)))