import math

def solution(progresses, speeds):
    remain = []
    n = len(progresses)
    for i in range(n):
        remain.append(math.ceil((100-progresses[i])/speeds[i]))

    cnt = 1
    tmp = remain[0]
    answer = []
    for i in range(1, n):
        if remain[i] <= tmp:
            cnt += 1
        else:
            answer.append(cnt)
            tmp = remain[i]
            cnt = 1
    
    answer.append(cnt)
    return answer