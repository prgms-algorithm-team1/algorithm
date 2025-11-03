import heapq


def solution(board):
    n = len(board)
    INF = 10 ** 12
    costs = [[[INF] * 4 for _ in range(n)] for _ in range(n)]

    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    hq = []

    for d in (1, 2):
        nr = 0 + dr[d]
        nc = 0 + dc[d]
        if 0 <= nr < n and 0 <= nc < n and board[nr][nc] == 0:
            costs[nr][nc][d] = 100
            heapq.heappush(hq, (100, nr, nc, d))

    while hq:
        cost, r, c, d = heapq.heappop(hq)
        if cost > costs[r][c][d]:
            continue
        if r == n - 1 and c == n - 1:
            return cost
        for nd in range(4):
            nr = r + dr[nd]
            nc = c + dc[nd]
            if not (0 <= nr < n and 0 <= nc < n):
                continue
            if board[nr][nc] == 1:
                continue
            add = 100 if nd == d else 600
            ncost = cost + add
            if ncost < costs[nr][nc][nd]:
                costs[nr][nc][nd] = ncost
                heapq.heappush(hq, (ncost, nr, nc, nd))

    return min(costs[n - 1][n - 1])
