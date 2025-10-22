def solution(prices):
    n = len(prices)
    answer = [0]*n
    stack = []

    for i, price in enumerate(prices):
        # 가격이 떨어진 기능 처리
        # stack의 마지막 요소의 price와 비교하고
        # 더 작으면 pop하여 작아진 시점의 index에서 stack에서 pop한 튜플의 index를 빼서
        # answer[idx]의 값을 변경한다.
        while stack and price < stack[-1][1]:
            idx, _ = stack.pop()
            answer[idx] = i - idx

        # stack에 index와 가격을 튜플로 append
        stack.append((i, price))

    # 끝까지 가격이 안 떨어진 기능 처리
    # 끝가지 가격이 떨어지지 않았으므로
    # 배열의 길이에서 1을 빼야 현재 idx에서 남은 시간을 알 수 있고 
    # idx를 빼면 얼마나 떨어지지 않았는지 알 수 있다.
    for idx, _ in stack:
        answer[idx] = n - idx - 1

    return answer

print(solution([1, 2, 3, 2, 3]))