n = int(input())
board = [list(input()) for _ in range(n)]
result = 0
direction = [[-1, 0], [1, 0], [0,-1], [0, 1]] 