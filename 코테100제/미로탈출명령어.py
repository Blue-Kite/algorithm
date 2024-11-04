def solution(n, m, x, y, r, c, k):
    direction = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    dname = ["l", "r", "u", "d"]

    #경로를 찾는 것이 불가능한 경우 
    dist =  abs(r-x) + abs(c-y)
    if dist > k or (dist-k) % 2 != 0:
        return "impossible"
    answer = 'z'


    def dfs(cnt, path, dx, dy):
        
        #dfs를 더 이상해도 의미 없음 
        if  k < cnt + dist:
            return 
        if dx == r and dy == c and cnt == k:
            return path
        
        else:
            for i in range(4):
                nx = dx + direction[i][0]
                ny = dy + direction[i][1]

                if 0<= nx < n and 0<= ny < n:
                   rtn = dfs(cnt+1, path+dname[i], nx, ny ) 
                   if rtn is not None and rtn < answer:
                        answer = rtn 

    dfs(0, '', x, y)
    return answer