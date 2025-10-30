from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    # 우선 시작점과 레버 도착점을 먼저 찾습니다.
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                start = (i, j)
            elif maps[i][j] == 'L':
                lever = (i, j)
            elif maps[i][j] == 'E':
                end = (i, j)

    def bfs(sx, sy, ex, ey):
        visited = [[False]*m for _ in range(n)]
        queue = deque()
        queue.append((sx, sy, 0))
        visited[sx][sy] = True
        
        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]
        
        while queue:
            x, y, dist = queue.popleft()
            # 좌표가 끝 좌표와 같은 현재까지 이동거리를 반환
            if (x, y) == (ex, ey):
                return dist  
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                # 방향 배열을 이용해서 이동 가능하거나 방문하지 않았을 경우 방문처리 후 거리 값 1증가
                if 0 <= nx < n and 0 <= ny < m:
                    if not visited[nx][ny] and maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        queue.append((nx, ny, dist+1))
        
        return -1  
    
    # 시작점에서 레버까지의 최단거리를 구합니다.
    dist1 = bfs(start[0], start[1], lever[0], lever[1])
    if dist1 == -1:
        return -1
    
    # 레버에서 도착지점까지의 최단거리를 구합니다.
    dist2 = bfs(lever[0], lever[1], end[0], end[1])
    if dist2 == -1:
        return -1
    
    return dist1 + dist2
