def solution(N, stages): 
    stages = list(map(int, stages)) 
    answer = [] 
    l = len(stages) 
    arr = [] 
    
    for i in range(1, N + 1):
        c = stages.count(i)
        if l > 0:
            arr.append((c / l, i)) 
            l -= c 
        else: 
            arr.append((0, i)) 
    
    arr.sort(key=lambda x: x[0], reverse=True) 
    answer = [x[1] for x in arr] 
    return answer