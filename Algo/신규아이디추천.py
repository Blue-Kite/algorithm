def solution(new_id):
    answer = ''
    #1단계 소문자 치환
    new_id = new_id.lower()
    #2단계 특정 문자 제거
    for c in new_id:
        if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
            answer += c

    #3단계 .. 이상일때 .로 치환  
    # replace 함수  문자열.replace(originStr, replaceStr, maxCount)
    while '..' in answer:
        answer = answer.replace('..', '.')

    #4단계 맨앞 맨뒤 .이면 제거
    if answer and answer[0] == '.':
        answer = answer[1:]
    if answer and answer[-1] == ".":
        answer = answer[:-1]

    if answer =='':
        answer = 'a'
    #6단계
    if len(answer)>=16:
        answer = answer[0:15]
    if answer[-1] == ".":
        answer = answer[0:14]

    if len(answer) <= 2:
        c = answer[-1]
        while len(answer) < 3:
            answer += c
    return answer

new_id = "...!@BaT#*..y.abcdefghijklm"
solution(new_id)