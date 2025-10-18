def solution(answers):
    student1 = [1,2,3,4,5]
    student2 = [2,1,2,3,2,4,2,5]
    student3 = [3,3,1,1,2,2,4,4,5,5]
    
    answer = [0,0,0]
    for i,x in enumerate(answers):
        if student1[i%5] == x:
            answer[0] += 1
            
        if student2[i%8] == x:
            answer[1] += 1
        
        if student3[i%10] == x:
            answer[2] += 1
            
    max_answer = max(answer)
    
    return [x+1 for x in range(3) if answer[x] == max_answer]