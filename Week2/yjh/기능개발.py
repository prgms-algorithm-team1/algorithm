def solution(progresses, speeds):
    days = [ (100 - p + s - 1) // s for p, s in zip(progresses, speeds) ]

    answer = []
    current = days[0]   
    cnt = 1             

    for d in days[1:]:
        if d <= current:
            cnt += 1
        else:
            answer.append(cnt)
            current = d
            cnt = 1

    answer.append(cnt)
    return answer
