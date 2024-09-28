#이분탐색
#https://suri78.tistory.com/209

#k번째수는 k보다 클 수 없는가? 1행이 존재해서 숫자가 겹치면 오히려 k번째는 더 작아짐 

n = int(input())
k = int(input())
result = n*n
s, e = 1, k

while s <= e:
    m = (s+e) // 2 
    cnt = 0 #cnt보다 작은 수들의 개수 

    for i in range(1, n+1):
        cnt += min(m//i, n) #i번째 행(i의 배수들)에서 m보다 작은 수들의 개수 최대 n개라서

    if cnt >= k:
        result = min(result, m)
        e = m -1
    else:
        s = m+1
        
print(result)


'''
이건 왜 안될까?
if cnt > k:
        e = m -1
elif cnt < k:
        s = m+1
else:
    result = m

'''