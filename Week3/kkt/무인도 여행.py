from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    
    visited = [[False] * m for i in range(n)]
    
    answer = []
    def BFS(i,j):
        visited[i][j] = True
        queue = deque()
        queue.append((i,j))
        total = int(maps[i][j])
        
        while queue:
            x,y = queue.popleft()
            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0<=sx<n and 0<=sy<m and maps[sx][sy] != "X" and not visited[sx][sy]:
                    queue.append((sx,sy))
                    visited[sx][sy] = True
                    total += int(maps[sx][sy])
                    
        answer.append(total)
        
    for i in range(n):
        for j in range(m):
            if maps[i][j] != "X" and not visited[i][j]:
                BFS(i,j)
    
    if not answer:
        return [-1]
    
    answer.sort()
    return answer