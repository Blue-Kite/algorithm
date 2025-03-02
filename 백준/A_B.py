from collections import deque
a, b = map(int, input().split())

#일종의 최단거리 -> bfs
def solve(a, b):
    q = deque()
    q.append([a, 1])

    while q:
        now, cnt = q.popleft()
        if now == b:
            return cnt

        if now * 2 <= b:
            q.append([now*2, cnt+1])

        if now * 10 + 1 <= b:
            q.append((now * 10 + 1, cnt + 1))
    return -1

print(solve(a,b))