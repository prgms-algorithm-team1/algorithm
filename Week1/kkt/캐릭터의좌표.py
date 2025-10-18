def solution(keyinput, board):
    directions = {
        "left":  (-1, 0),
        "right": (1, 0),
        "down":  (0, -1),
        "up":    (0, 1)
    }
    
    pos = [0,0]
    n,m = board[0]//2,board[1]//2
    for op in keyinput:
        dx,dy = directions[op]
        x,y = pos
        
        sx,sy = x+dx,y+dy
        if abs(sx)<=n and abs(sy)<=m:
            pos = [sx,sy]
        
    return pos