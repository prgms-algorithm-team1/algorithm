def solution(keyinput, board):
    x = 0
    y = 0
    xmax = board[0]
    ymax = board[1]

    move = {
        "left":  (-1, 0),
        "right": ( 1, 0),
        "up":    ( 0, 1),
        "down":  ( 0,-1),
    }

    for k in keyinput:
        if k not in move:
            continue
        dx, dy = move[k]
        nx, ny = x + dx, y + dy
        if -xmax <= nx <= xmax and -ymax <= ny <= ymax:
            x, y = nx, ny

    return [x, y]
