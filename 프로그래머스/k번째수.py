def solution(array, commands):
    answer = []
    for i,j,k in commands:
        array_copy = [i for i in array]
        new_array = array[i-1:j]
        new_array.sort()
        answer.append(new_array[k-1])
    return answer