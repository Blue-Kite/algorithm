#https://www.acmicpc.net/problem/1406
#시간초과가 나서 수정이 필요
#https://seongonion.tistory.com/53

#스택: https://www.acmicpc.net/problem/10828
#큐: https://www.acmicpc.net/problem/10845

s = list(input())
n = len(s)
m = int(input())
cmds = []
cursor = n

for i in range(m):
    cmds.append(input().split())

for cmd in cmds:
    if cmd[0] == 'P':
        s.insert(cursor, cmd[1])
        cursor += 1
    elif cmd[0] == 'L':
        if cursor > 0:
            cursor -= 1

    elif cmd[0] == 'D':
        if cursor < len(s):
            cursor += 1
    else:
        if cursor > 0:
            s.remove(s[cursor-1])
print(''.join(s))