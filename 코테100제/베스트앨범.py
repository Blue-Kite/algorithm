#가장 많이 재생된 장르 리스트 필요
#장르별 곡 정보 필요 

def solution(genres, plays):
    answer = []
    songlist = {}
    playlist = {}
    n = len(plays)

    for i in range(n):
        if genres[i] not in playlist:
            playlist[genres[i]] = 0
            songlist[genres[i]] = []

        playlist[genres[i]] += plays[i]
        songlist[genres[i]].append([plays[i], i])
    
    #value기준으로 정렬 
    play_sort = sorted(playlist.items(), key=lambda x: x[1], reverse=True)
    

    for genre in play_sort:
        song_sort = sorted(songlist[genre[0]], key=lambda x : (-x[0], x[1]))
        for s in song_sort[:2]:
            answer.append(s[1])
    return answer