# 내가 누구를 신고했는지
# 각 유저별로 몇번 신고당했는지 
# 리스트 to 딕셔너리 https://security-nanglam.tistory.com/427
def solution(id_list, report, k):
    answer = []
    id_report = {id:[] for id in id_list}
    id_howmanyreport = {id:0 for id in id_list}
    resultid = []

    for i in report:
        thelist = i.split() #공백으로 문자열 구분, 리스트 반환 
        id = thelist[0]
        badid = thelist[1]

        id_howmanyreport[badid] += 1
        id_report[id].append(badid)
    
    for id in id_howmanyreport.keys():
        if id_howmanyreport[id] >= k:
            resultid.append(id)

    i = 0
    for id in id_report.keys:
        for badid in resultid:
            if badid in id_report[id]:
                answer[i] += 1
        i += 1