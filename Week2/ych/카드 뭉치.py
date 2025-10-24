def solution(cards1, cards2, goal):
    # 카드 뭉치에는 각각 단어 카드들이 들어있음
    # 각 카드는 순서대로만 사용 가능 (같은 카드뭉치 내에서 순서 건너뛰기 불가)
    # goal을 만들 수 있으면 Yes, 아니면 No
    idx1 = 0  # cards1의 현재 위치
    idx2 = 0  # cards2의 현재 위치
    
    for word in goal:
        if idx1 < len(cards1) and cards1[idx1] == word:
            idx1 += 1  # cards1에서 사용
        elif idx2 < len(cards2) and cards2[idx2] == word:
            idx2 += 1  # cards2에서 사용
        else:
            return "No"  # 둘 다 안 맞으면 실패
    
    return "Yes"
