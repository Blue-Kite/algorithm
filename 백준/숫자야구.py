from itertools import permutations

n = int(input())
baseball = []
for _ in range(n):
    baseball.append(list(map(int, input().split())))

nums = [1,2,3,4,5,6,7,8,9]
numlist = list(permutations(nums, 3))
answer = 0

for candidate in numlist:
    #candidate: 후보 3자리 숫자 
    flag = True
    for query in baseball:
        a, b = 0, 0
        qnum = list(map(int,str(query[0]))) 
        strike = query[1]
        ball = query[2]

        for i in range(3):
            if candidate[i] == qnum[i]:
                a += 1 

            else:
                if candidate[i] in qnum:
                    b += 1

        #스트라이크 개수 틀림 or 볼 개수 틀림
        if a != strike or b != ball:
            flag = False
            break 

    if flag:
        answer += 1

print(answer)

