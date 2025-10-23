def solution(N, stages):
    answer = []
    all_num = len(stages)
    num = {}

    for i in range(1, N+1) :
        cnt = 0
        for step in stages :
            if step == i:
                cnt += 1
        if cnt == 0 :
            num[i] = 0
        else :
            num[i] = (cnt/all_num)
            
        all_num = all_num - cnt
        
    return sorted(num, key = lambda x : num[x], reverse = True)