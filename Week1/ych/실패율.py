def solution(N, stages):
    # 스테이지에 도달했으나 아직 클리어 못한 플레이어 수는 stages에서 같은 수의 개수로 계산
    # 스테이지에 도달한 플레이어는 그 수보다 같거나 큰 stages 수의 개수로 계산
    # N+1은 모든 스테이지 클리어한거임
    
    lst = []
    for i in range(N + 1):
        a = stages.count(i + 1)
        lst.append(a) # [1, 3, 2, 1, 0, 1]
    # 스테이지 도달한 사용자는 현재 수보다 같거나 큼
    
    total = 0
    for i in lst:
        total += i
    
    lst_2 = []
    for i in range(N):
        if total == 0:
            b = 0
        else:
            b = float(lst[i]) / float(total)
        print(lst[i], total, b)
        lst_2.append(b)
        total -= lst[i]
    
    result = []
    for i in range(N):
        result.append((i + 1, lst_2[i]))  # (스테이지 번호, 실패율)
    
    # 실패율 기준 내림차순 정렬
    result.sort(key=lambda x: x[1], reverse=True)
    
    # 스테이지 번호만 추출
    answer = [stage for stage, fail_rate in result]

    return answer