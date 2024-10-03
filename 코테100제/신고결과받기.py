#신고당한사람(키) - 신고한 사람(list, value) 로 한 이유?
#value 길이로 신고 횟수, 나중에 누구한테 보낼지 관리 가능

def solution(id_list, report, k):
    answer = []
    countdict = {}
    reportdict = {}

    for r in report:
        angry, bad = r.split()
        if bad not in reportdict:
            reportdict[bad] = set()

        reportdict[bad].add(angry)
    
    for id in id_list:
        if id in reportdict and len(reportdict[id]) >= k:
            for angry in reportdict[id]:
                if angry not in countdict:
                    countdict[angry] = 1
                else:
                    countdict[angry] += 1
    for id in id_list:
        if id in countdict:
            answer.append(countdict[id])
        else:
            answer.append(0)
    return answer