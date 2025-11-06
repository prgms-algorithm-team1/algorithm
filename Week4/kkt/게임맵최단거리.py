from collections import deque

def solution(maps):
    n =len(maps)
    m = len(maps[0])
    directions = [(1,0),(-1,0),(0,1),(0,-1)]
    def BFS():
        queue = deque()
        queue.append((0,0,1))
        visited = [[False] * m for i in range(n)]
        visited[0][0] = True
        
        while queue:
            x,y,cnt = queue.popleft()
            if x == n-1 and y == m-1:
                return cnt
            
            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0<=sx<n and 0<=sy<m and maps[sx][sy] and not visited[sx][sy]:
                    queue.append((sx,sy,cnt+1))
                    visited[sx][sy] = True
                    
        return -1
    
    return BFS()