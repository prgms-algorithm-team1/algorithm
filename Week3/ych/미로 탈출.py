from collections import deque


def solution(maps):
    h = len(maps)
    w = len(maps[0])

    start = lever = exit_ = None
    for i in range(h):
        for j in range(w):
            cell = maps[i][j]
            if cell == 'S':
                start = (i, j)
            elif cell == 'L':
                lever = (i, j)
            elif cell == 'E':
                exit_ = (i, j)

    def bfs(src, dst):
        q = deque()
        visited = [[False] * w for _ in range(h)]
        q.append((src[0], src[1], 0))
        visited[src[0]][src[1]] = True

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            x, y, d = q.popleft()
            if (x, y) == dst:
                return d
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        q.append((nx, ny, d + 1))
        return -1

    d1 = bfs(start, lever)
    if d1 == -1:
        return -1
    d2 = bfs(lever, exit_)
    if d2 == -1:
        return -1
    return d1 + d2
