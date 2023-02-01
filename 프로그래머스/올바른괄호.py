def solution(s):
    answer = True
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        else:
            if not stack:
                return False
            else:
                #괜히 pop(0)으로 하면 효율성 초과 뜸 
                stack.pop()
    if len(stack) != 0:
        answer = False
    return answer