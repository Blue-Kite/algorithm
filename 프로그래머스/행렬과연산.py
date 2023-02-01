"""
총 10만개라서 shift이든 rotate이든 연산이 n(1) or n(logn)의 
복잡도를 가져야만한다. => deque o(1)
"""
"""
https://s3.us-west-2.amazonaws.com/secure.notion-static.com/b137a828-f6ba-4d7d-bd21-b57c8f43b0c9/%E1%84%91%E1%85%B3%E1%84%85%E1%85%A9%E1%84%80%E1%85%B3%E1%84%85%E1%85%A2%E1%84%86%E1%85%A5%E1%84%89%E1%85%B3_%E1%84%92%E1%85%A2%E1%86%BC%E1%84%85%E1%85%A7%E1%86%AF%E1%84%80%E1%85%AA%E1%84%8B%E1%85%A7%E1%86%AB%E1%84%89%E1%85%A1%E1%86%AB.py?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=AKIAT73L2G45EIPT3X45%2F20230131%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20230131T024336Z&X-Amz-Expires=86400&X-Amz-Signature=a50d21672ad6093469aab62658f6d04bfb3e247e5242822a31b7bd1bd7f6db20&X-Amz-SignedHeaders=host&response-content-disposition=filename%3D%22%25E1%2584%2591%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25A9%25E1%2584%2580%25E1%2585%25B3%25E1%2584%2585%25E1%2585%25A2%25E1%2584%2586%25E1%2585%25A5%25E1%2584%2589%25E1%2585%25B3_%25E1%2584%2592%25E1%2585%25A2%25E1%2586%25BC%25E1%2584%2585%25E1%2585%25A7%25E1%2586%25AF%25E1%2584%2580%25E1%2585%25AA%25E1%2584%258B%25E1%2585%25A7%25E1%2586%25AB%25E1%2584%2589%25E1%2585%25A1%25E1%2586%25AB.py%22&x-id=GetObject

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
