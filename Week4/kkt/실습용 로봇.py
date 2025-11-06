def solution(command):
    d = 0
    x,y = 0,0
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    for op in command:
        if op == "R":
            d = (d+1)%4
        elif op == "L":
            d = (d-1)%4   
        elif op == "G":
            x += directions[d][0]
            y += directions[d][1]
        elif op == "B":
            x -= directions[d][0]
            y -= directions[d][1]
            
    return [x,y]