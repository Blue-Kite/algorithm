def solution(arr1, arr2):
    r1, r2 = len(arr1), len(arr1[0])
    r3, r4 = len(arr2), len(arr2[0])
    answer = [[0 for _ in range(r4)] for _ in range(r1)]
    
    for i in range(r1):
        for j in range(r4):
            for k in range(r2):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer