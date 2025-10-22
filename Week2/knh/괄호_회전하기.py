from collections import deque

def solution(s):
    answer = 0
    x = len(s)
    dq = deque(s)

    for _ in range(x):
        # 제일 왼쪽 거를 pop해서 마지막에 append
        dq.append(dq.popleft())
        # deque을 문자로  
        rotated_string = ''.join(dq)

        stack = []
        # 문자 확인
        for ch in rotated_string:
            # 여는 괄호의 경우 append
            if ch == '(' or ch == '{' or ch == '[':
                stack.append(ch)
            # 닫는 괄호의 경우
            elif ch == ')':
                # stack이 비었거나 짝이 맞는 여는 괄호가 아닐 경우
                if not stack or stack[-1] != '(':
                    # 아무것도 넣지 않으면 빈 스택이라 count가 +1 되므로 임의의 값 'x'를 append
                    stack.append('x')
                    break
                # 짝이 맞으면 stack에서 제거
                stack.pop()
            elif ch == '}':
                if not stack or stack[-1] != '{':
                    stack.append('x')
                    break
                stack.pop()
            elif ch == ']':
                if not stack or stack[-1] != '[':
                    stack.append('x')
                    break
                stack.pop()
            else:
                stack.append('x')
                break
        # stack에 값이 비었으면 여는 괄호와 닫는 괄호가 모두 짝이 맞는 경우이므로 answer에 1을 더함
        if not stack:
            answer += 1

    return answer
