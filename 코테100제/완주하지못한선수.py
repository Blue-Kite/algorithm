def solution(participant, completion):
    pdict = {}
    for p in participant:
        if p in pdict:
            pdict[p] += 1
        else:
            pdict[p] = 1
    
    for c in completion:   
        if c in pdict:
            pdict[c] -= 1

    for pkey in pdict:
        if pdict[pkey] > 0:
            return pkey
        
    