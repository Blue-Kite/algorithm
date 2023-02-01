from itertools import combinations
n = int(input())
nums = []

for i in range(1, 11): #조합의 길이 1~10
    for comb in combinations(range(0, 10), i): #조합을 만들 리스트 [0... 9] 
        comb = list(comb)
        comb.sort(reverse=True)                #감소하는 수          
        nums.append(int("".join(map(str, comb)))) #[9, 7, 1] 를 묶어서 하나의 수로

nums.sort() 
try:
    print(nums[n])
except:
    print(-1)