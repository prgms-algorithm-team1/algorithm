def solution(cards1, cards2, goal):
    idx1 = 0
    idx2 = 0
    for i in range(len(goal)):
        if idx1 < len(cards1) and goal[i] == cards1[idx1]:
            idx1 += 1
            
        elif idx2 < len(cards2) and goal[i] == cards2[idx2]:
            idx2 += 1
            
        else:
            return "No"
    
    return "Yes"