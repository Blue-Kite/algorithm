'''
    https://www.ai-bio.info/programmers/77886
    110을 문자열에 삽입해서 새로 110이 나타나는 경우가 없음 오...!
    모든 110를 찾아서 
    가장 왼쪽 111의 앞에 삽입 
'''
def solution(s):
    answer = []

    for word in s:
        n = len(word)
        stack, num110 = [], 0
        for i in range(n):
            if word[i] == '0':
                if len(stack) >= 2 and stack[-1] == '1' and stack[-2] == '1':
                    stack.pop()
                    stack.pop()
                    num110 += 1
                else:
                    stack.append(word[i])
            else:
                stack.append(word[i])    
        
        #이 아래가 중요...
        w = ''.join(stack)
        idx = w.rfind('0')
        new_w = ''
        if idx == -1:
            new_w = '110' * num110 + w
        else:
            new_w = w[:idx+1] + '110' * num110 + w[idx+1:]
        answer.append(new_w)
    return answer