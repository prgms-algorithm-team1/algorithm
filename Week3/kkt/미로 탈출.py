from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i,j)
                
            elif maps[i][j] == "L":
                lever = (i,j)
                
    directions = [(1,0),(-1,0),(0,1),(0,-1)]    
    
    def BFS(push_lever, pos):
        visited = [[False] * m for i in range(n)]  
        i,j = pos
        queue = deque([(i,j,0)])
        while queue:
            x,y,cnt = queue.popleft()
            for dx,dy in directions:
                sx,sy = x+dx,y+dy
                if 0<=sx<n and 0<=sy<m and not visited[sx][sy]:
                    if push_lever:
                        if maps[sx][sy] in ["O","L","S"]:
                            queue.append((sx,sy,cnt+1))
                            visited[sx][sy] = True
                            
                        elif maps[sx][sy] == "E":
                            return cnt + 1
                        
                    else:
                        if maps[sx][sy] in ["O","E","S"]:
                            queue.append((sx,sy,cnt+1)) 
                            visited[sx][sy] = True
                            
                        elif maps[sx][sy] == "L":
                            return cnt + 1
        
        return 0
    
    answer = 0
    before_lever = BFS(False,start)
    if not before_lever:
        return -1
    
    answer += before_lever
    after_lever = BFS(True, lever)
    if not after_lever:
        return -1
    
    answer += after_lever
    return answer