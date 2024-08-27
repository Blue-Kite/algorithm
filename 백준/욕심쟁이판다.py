n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))

def recur(i, j):
    direction=[[0, -1], [0, 1], [-1, 0], [1, 0]]
    result = 0

    for k in range(4):
        dx = i + direction[i][0]
        dy = j + direction[i][1]

        if 0 <= dx < n and 0 <= dy < n:
            if nums[i][j] < nums[dx][dy]:
                return max(result, recur(dx, dy) + 1)
    return 0

for i in range(n):
    for j in range(n):
        result = recur(i, j)

print(result)