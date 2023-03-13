def solution(record):
    answer = []
    nickname = {}
    msg = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    for r in record:
        rsplit = r.split()
        #Enter이거나 leave인 경우
        if len(rsplit) == 3:
            nickname[rsplit[1]] = rsplit[2]
    for r in record:
        rsplit = r.split()
        if rsplit[0] == "Enter":
            answer.append(nickname[rsplit[1]]+ msg[rsplit[0]])
        if rsplit[0] == "Leave":
            answer.append(nickname[rsplit[1]]+ msg[rsplit[0]])
    
    return answer