def solution(board, moves):
    basket = []
    removed = 0
    n = len(board)
    cols = [[] for _ in range(n)]
    for c in range(n):
        for r in range(n - 1, -1, -1):
            if board[r][c] != 0:
                cols[c].append(board[r][c])

    for m in moves:
        c = m - 1
        if not cols[c]:
            continue  
        doll = cols[c].pop() 

        if basket and basket[-1] == doll:
            basket.pop()
            removed += 2
        else:
            basket.append(doll)

    return removed
