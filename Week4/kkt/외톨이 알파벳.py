def solution(input_string):
    visited = set()
    
    tmp = input_string[0]
    visited.add(tmp)
    
    answer_set = set()
    answer = []
    for s in input_string:
        if tmp == s:
            continue
        
        tmp = s
        if s in visited and s not in answer_set:
            answer.append(s)
            answer_set.add(s)

        visited.add(s)
        
    if not answer:
        return "N"
    
    return "".join(sorted(answer))