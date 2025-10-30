from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])
    
    # S, L, E 위치 찾기
    start, lever, end = None, None, None
    for r in range(rows):
        for c in range(cols):
            if maps[r][c] == 'S':
                start = (r, c)
            elif maps[r][c] == 'L':
                lever = (r, c)
            elif maps[r][c] == 'E':
                end = (r, c)

    # BFS 함수 정의
    def bfs(start_pos, target_pos):
        # 큐: (현재 위치 r, 현재 위치 c, 이동 시간)
        queue = deque([(start_pos[0], start_pos[1], 0)])
        # 방문 여부 및 최단 시간 기록 (rows x cols 크기의 2차원 배열)
        # 초기값은 모두 False (방문하지 않음)
        visited = [[False] * cols for _ in range(rows)]
        visited[start_pos[0]][start_pos[1]] = True  # 시작 지점 방문 처리
        
        # 상, 하, 좌, 우 이동 방향
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        
        while queue:
            r, c, time = queue.popleft()
            
            # 목표 지점에 도달하면 시간 반환
            if r == target_pos[0] and c == target_pos[1]:
                return time
            
            # 4가지 방향으로 이동
            for i in range(4):
                nr, nc = r + dr[i], c + dc[i]
                
                # 맵 범위 체크
                if 0 <= nr < rows and 0 <= nc < cols:
                    # 벽('X')이 아니고, 아직 방문하지 않은 곳이라면
                    if maps[nr][nc] != 'X' and not visited[nr][nc]:
                        visited[nr][nc] = True  # 방문 처리
                        queue.append((nr, nc, time + 1)) # 큐에 추가 (시간 + 1)
        
        # 목표 지점에 도달할 수 없다면 -1 반환
        return -1

    # 1. 시작(S) -> 레버(L)까지의 최단 거리 계산
    time1 = bfs(start, lever)
    
    # 레버에 도달할 수 없는 경우
    if time1 == -1:
        return -1

    # 2. 레버(L) -> 출구(E)까지의 최단 거리 계산
    time2 = bfs(lever, end)
    
    # 출구에 도달할 수 없는 경우
    if time2 == -1:
        return -1

    # 두 최단 거리를 합산하여 최종 결과 반환
    return time1 + time2
