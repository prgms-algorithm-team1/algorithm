import math

def solution(progresses, speeds):
    if not progresses:
        return []
    # progresses를 한 바퀴 다 돌면서
    # (100 - progresses[i]) / speeds[i] -> 올림 한 게 정상 배포일
    lst = []
    for i in range(len(progresses)):
        lst.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    answer = []
    count = 1
    standard = lst[0]
    for i in range(1, len(lst)):
        if lst[i] <= standard:
            count += 1
        else:
            answer.append(count)
            count = 1
            standard = lst[i]
    answer.append(count)

    return answer