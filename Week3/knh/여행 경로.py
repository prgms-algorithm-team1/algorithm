def solution(tickets):
    # 티켓을 정렬합니다. 사전 순으로 작은 것부터 큰 것까지.
    tickets.sort(key=lambda x: x[1])  # 두 번째 항목(도착지)을 기준으로 정렬
    
    # 여행 경로를 저장할 리스트
    path = []
    
    def dfs(current, visited):
        # 경로에 현재 공항을 추가
        path.append(current)
        
        # 모든 티켓을 다 사용했다면, 탐색을 종료
        if len(visited) == len(tickets):
            return True
        
        # 티켓을 하나씩 사용해보면서 재귀적으로 탐색
        for i, (start, end) in enumerate(tickets):
            if i not in visited and start == current:
                visited.add(i)
                if dfs(end, visited):
                    return True
                visited.remove(i)  # 백트래킹
        
        # 탐색이 끝났을 경우 경로를 되돌리기
        path.pop()
        return False
    
    # 처음 ICN에서 출발하여 DFS 탐색 시작
    visited = set()
    dfs("ICN", visited)
    
    return path

# 테스트
tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
print(solution(tickets))  # ["ICN", "JFK", "HND", "IAD"]
