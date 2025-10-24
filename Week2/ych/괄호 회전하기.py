def solution(s):
    answer = 0
    for i in range(len(s)):
        rotated = s[i:] + s[:i]
        if is_valid(rotated):
            answer += 1
    return answer

def is_valid(s):
    lst = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for char in s:
        if char in '({[': 
            lst.append(char)
        else:
            if not lst:  # 스택이 비어있으면 실패
                return False
            if pairs[lst[-1]] == char:  # 짝이 맞으면
                lst.pop()
            else:  # 안 맞으면 실패
                return False
    
    return len(lst) == 0  # 스택이 비어야 성공
