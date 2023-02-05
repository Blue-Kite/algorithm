"""
총 10만개라서 shift이든 rotate이든 연산이 n(1) or n(logn)의 
복잡도를 가져야만한다. => deque o(1)
"""
"""
rotate 의 문제
https://velog.io/@kevin622/Programmers-%ED%96%89%EB%A0%AC%EA%B3%BC-%EC%97%B0%EC%82%B0-2022-KAKAO-TECH-INTERNSHIP
"""

from collections import deque

def solution(rc, operations):
    answer = [[]]
    r_len, c_len = len(rc), len(rc[0])

    left = deque(rc[r][0] for r in range(r_len))
    right = deque(rc[r][c_len - 1] for r in range(r_len))
    midrow = deque(deque(row[1:-1]) for row in rc)


    for op in operations:
        if op == "Rotate":
            right.appendleft(midrow[0].pop())
            midrow[0].appendleft(left.popleft())
            left.append(midrow[-1].popleft())
            midrow[-1].append(right.pop())

        else:
            midrow.appendleft(midrow.pop())
            left.appendleft(left.pop())
            right.appendleft(right.pop())

        print(op)
        print(left)
        print(midrow)
        print(right)
        print(answer)
    #return answer
