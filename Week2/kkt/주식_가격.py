def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = []
    
    i= 0
    for price in prices:
        while stack and price < stack[-1][1]:
            idx, p = stack.pop()
            answer[idx] = i - idx
        
        stack.append((i,price))
        i += 1
    
    while stack:
        idx, p = stack.pop()
        answer[idx] = n - 1 - idx
    
    return answer