#220514
#백준 14719 빗물 
#https://www.acmicpc.net/problem/14719

# https://velog.io/@kynel/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%EB%B9%97%EB%AC%BC-%ED%8A%B8%EB%9E%98%ED%95%91


h, w = map(int, input().split()) #블록 쌓인거 최대 높이 h 블록수 w 
blocks = list(map(int, input().split()))
answer = 0
stack = []

if not blocks:
    print(answer)
    exit()

for i in range(w):
    if i == 0:  #첫번째 블록 
        startblock = blocks[i]
    elif blocks[i] < startblock:
        stack.append(blocks[i])
    else: #blocks[i] >= startblock
        endblock = blocks[i]
        while stack:
            b = stack.pop()
            answer += (min(endblock, startblock) - b)   
        startblock = blocks[i]

  
endblock = blocks[-1]
while stack:
  b = stack.pop()
  answer += (min(endblock, startblock) - b)    
print(answer)

