def solution(tickets):
    # 1. 티켓 정렬: 알파벳 순서가 앞서는 경로를 먼저 탐색하기 위해 도착지를 기준으로 정렬
    # (출발지가 같을 경우, 도착지가 알파벳 순으로 빠른 것을 먼저 보게 됨)
    tickets.sort(key=lambda x: x[1])
    
    # 총 티켓의 개수 (경로의 길이는 이보다 1 큼)
    N = len(tickets)
    
    # 사용 여부를 체크할 배열
    used = [False] * N
    
    # 결과를 담을 리스트. 시작은 항상 "ICN"
    route = ["ICN"]
    
    def dfs(current_airport):
        # 경로 완성 조건: 모든 티켓을 사용했을 때
        if len(route) == N + 1:
            return True # 경로 완성 성공!

        # 모든 티켓을 순회하며 다음 경로 탐색
        for i in range(N):
            # 현재 티켓을 사용하지 않았고, 현재 공항에서 출발하는 티켓이라면
            if not used[i] and tickets[i][0] == current_airport:
                
                # 1. 티켓 사용 (전진)
                used[i] = True
                route.append(tickets[i][1]) # 경로에 도착 공항 추가
                
                # 2. 다음 공항으로 DFS 탐색
                if dfs(tickets[i][1]):
                    # 성공적으로 경로가 완성되면 True 반환 (더 이상 다른 경로는 찾을 필요 없음)
                    return True
                
                # 3. 백트래킹 (실패): 현재 경로가 막혔거나, 모든 티켓을 사용하지 못했으므로 되돌리기
                route.pop()    # 경로에서 도착 공항 제거
                used[i] = False # 티켓 사용 취소
                
        # 현재 공항에서 더 이상 갈 곳이 없거나, 모든 티켓을 사용하지 못했음
        return False

    # "ICN"에서 DFS 시작
    dfs("ICN")
    
    return route
