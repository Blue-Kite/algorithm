s = input()
stack = []
for i in range(26):
    w = chr(ord('a')+i)
    c = s.count(w)
    stack.append(c)

print(stack)


