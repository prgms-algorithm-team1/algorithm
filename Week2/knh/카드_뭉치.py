from collections import deque
def solution(cards1, cards2, goal):
    answer = "No"
    cards1, cards2 = deque(cards1), deque(cards2)
    count = 0
    for g in goal:
        # cards1가 있을 때
        if cards1:
            if g == cards1[0]:
                # 앞에 카드를 뺀다
                cards1.popleft()
                count += 1
                continue
        # cards2가 있을 때
        if cards2: 
            if g == cards2[0]:
                # 앞에 카드를 뺀다
                cards2.popleft()
                count += 1
                continue
    # goal의 길이와 card(N)[0]과 맞는 갯수가 같을 경우 조건 만족이므로 answer를 'Yes'로 재할당
    if count == len(goal):
        answer = "Yes"
    print(count)
    return answer