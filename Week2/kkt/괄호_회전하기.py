def solution(s):
    n = len(s)
    answer = 0
    
    for j in range(n):
        stack = []
        isWrong = False

        for i in range(n):
            x = s[i]
            if stack and ((stack[-1] == "(" and x == ")") or (stack[-1] == "[" and x == "]") or (stack[-1] == "{" and x == "}")):
                stack.pop()

            elif x in ["(","[","{"]:
                stack.append(x)

            else:
                isWrong = True
                break
        
        s = s[1:] + s[:1]
        
        if isWrong or stack:
            continue
        
        answer += 1
        
    
    return answer