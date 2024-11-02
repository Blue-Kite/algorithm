def solution(bandage, health, attacks):
    answer = 0
    time = 0
    flag = 0
    j = 0
    max_health = health
    
    while time <= attacks[-1][0]:
        time += 1
        
        if time == attacks[j][0]:
            health -= attacks[j][1]
            flag = 0
            j += 1
        else:
            health += bandage[1]
            flag += 1
            if flag == bandage[0]:
                health += bandage[2]
                flag = 0
                
        if health > max_health:
            health = max_health 
        if health <= 0:
            return -1
        if j == len(attacks):
            return health 
        