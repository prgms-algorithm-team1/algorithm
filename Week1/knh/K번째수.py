def solution(array, commands):
    answer = []
    for command in commands:
        c = list(map(int, command))
        i,j,k = c
        arr = sorted(array[i-1:j])
        answer.append(arr[k-1])
    return answer