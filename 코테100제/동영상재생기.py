#시간 계산 

def make_sec(time):
    m, s = map(int, time.split(":"))
    return m*60 + s

def make_str(time):
    if time < 10:
        return '0' + str(time)
    else:
        return str(time)


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len_n = make_sec(video_len)
    pos_n = make_sec(pos)
    op_start_n = make_sec(op_start)
    op_end_n = make_sec(op_end)

    #주의 
    if op_start_n <= pos_n <= op_end_n:
            pos_n = op_end_n 
            
    for c in commands:
        if c == "next": 
            pos_n += 10
        elif c == "prev":
            pos_n -= 10

        if pos_n < 0:
            pos_n = 0
        if pos_n > video_len_n:
            pos_n = video_len_n
        
        #이게 최우선 조건이라서 맨 밑에 있어야함 
        if op_start_n <= pos_n <= op_end_n:
            pos_n = op_end_n 
    
    res = [make_str(pos_n //60), make_str(pos_n % 60)]
    return ':'.join(res)