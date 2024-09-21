def solution(answers):
    answer = []
    pattern = [
        [1,2,3,4,5],
        [2,1,2,3,2,4,2,5],
        [3,3,1,1,2,2,4,4,5,5]
    ]
    score = [0] * 3

    for i, a in enumerate(answers):
        for j, p in enumerate(pattern):
            if a == p[i % len(p)]:
                score[j] += 1
                
    maxscore = max(score)
    
    for i, s in enumerate(score):
        if s == maxscore:
            answer.append(i+1)
    return answer