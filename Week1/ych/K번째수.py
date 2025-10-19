def solution(array, commands):
    answer = []
    for idx in range(len(commands)):
        i = commands[idx][0]
        j = commands[idx][1]
        k = commands[idx][2]
        
        lst = array[i-1:j]
        lst.sort()
        answer.append(lst[k-1])
        
    return answer
