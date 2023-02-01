import sys
s1 = list(sys.stdin.readline().rstrip())
s2 = []
n = len(s1)
m = int(sys.stdin.readline())
cmds = []
cursor = n

for _ in range(m):
    cmds.append(list(sys.stdin.readline().split()))

for cmd in cmds:
    if cmd[0] == 'L':
        if s1:
            s2.append(s1.pop())
    elif cmd[0] == 'D':
        if s2:
            s1.append(s2.pop())
    elif cmd[0] == 'B':
        if s1:
            s1.pop()
    else:
        s1.append(cmd[1])
s1.extend(reversed(s2))
print(''.join(s1))
