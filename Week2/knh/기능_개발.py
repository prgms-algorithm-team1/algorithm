from collections import deque

def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    answer = []

    while progresses:
        # 하루씩 진행
        # 각 기능에 speed만큼 더함
        # 하루 진행
        # [93, 30, 55] + [1,30,5] → [94, 60, 60]
        # 두 번째 날
        # [94, 60, 60] + [1,30,5] → [95, 90, 65]
        # 세 번째 날
        # [95, 90, 65] + [1,30,5] → [96, 120, 70]
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 배포 가능한 기능 확인
        # 7일차 전까지 progresses[0]이 100이상인 경우가 없어 while문이 실행되지 않음
        # 7일차: [100, 240, 90]
        # progresses,speeds가 pop되고 count += 1 함
        count = 0
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        # progresses[0]이 90이므로 while문이 끝나고
        # count 2가 answer 배열에 append 된다.
        if count > 0:
            answer.append(count)

    return answer