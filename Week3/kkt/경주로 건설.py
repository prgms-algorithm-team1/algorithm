from collections import deque

def solution(board):
    def BFS():
        n = len(board)
        queue = deque()
        queue.append((0,0,0,4))
        
        visited = [[[float("inf")] * 4 for i in range(n)] for i in range(n)]
        for i in range(4):
            visited[0][0][i] = 0
        
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        #prev 0 U 1 D 2 L 3 R 4 Start
        while queue:
            x,y,total,prev = queue.popleft()
            for i, (dx,dy) in enumerate(directions):
                sx,sy = x+dx, y+dy
                if 0<=sx<n and 0<=sy<n and board[sx][sy] == 0:
                    if prev == 4 or prev == i:
                        next_total = total + 100
                    else:
                        next_total = total + 600

                    if visited[sx][sy][i] > next_total:
                        visited[sx][sy][i] = next_total
                        queue.append((sx,sy,next_total,i))
        
        print(visited)
        return min(visited[n-1][n-1])
    
    return BFS()