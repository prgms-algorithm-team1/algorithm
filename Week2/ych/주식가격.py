def solution(prices):
    # 가격이 떨어지지 않은 기간은 몇 초?
    # prices = [1, 2, 3, 2, 3]
    # return = [4, 3, 1, 1, 0]
    # for i in range(len(prices)) 해가지고
    # prices[i] < prices[i+1] 이면 cnt가 1씩 추가
    # 아니면 i+1을 lst에 추가
    # 근데 이러면 이중 반복문인데... 
    answer = []
    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1, len(prices)):
            cnt += 1
            if prices[j] < prices[i]:
                break
        answer.append(cnt)
    return answer