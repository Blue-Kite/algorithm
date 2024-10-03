def solution(record):
    answer = []
    msg = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}
    userlist = {}

    for r in record: 
        cmd = r.split()
        if cmd[0] == 'Enter' or cmd[0] == 'Change':
            userlist[cmd[1]] = cmd[2] 

    for r in record:
        cmd = r.split()
        if cmd[0] in msg:
            m = userlist[cmd[1]] + msg[cmd[0]]
            answer.append(m)
    
    return answer