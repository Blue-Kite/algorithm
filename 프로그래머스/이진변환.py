def radixchange(n):
    radix = 2
    if n == 0:
        return '0'
    newN = []
    while n:
        n, digit = divmod(n, radix)
        newN.append(str(digit))
    newN.reverse()
    return ''.join(newN)
  
def removezero(n):
    newN = ''
    cnt = 0
    n = list(n)
    for i in n:
        if i == '0':
            cnt += 1
            continue
        else:
            newN += '1' 
    return newN, cnt

def solution(n):
    answer = [0, 0]
    cnt = 0
    zero = 0
    while len(n) > 1:
        newN, zero = removezero(n)
        answer[1] += zero
        n = radixchange(len(newN))
        cnt += 1
        answer[0] = cnt
    return answer