from collections import defaultdict
def solution(N, stages):
    stages_dict = defaultdict(int)

    for x in stages:
        stages_dict[x] += 1

    total = len(stages)

    result = []
    for i in range(1, N+1):
        if total > 0:
            result.append((i, stages_dict[i] / total))
            total -= stages_dict[i]

        else:
            result.append((i, 0))
    
    result.sort(key= lambda x:(-x[1],x[0]))

    return [x for x,_ in result]