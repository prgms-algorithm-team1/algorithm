from collections import deque


def solution(maps):
    h = len(maps)
    w = len(maps[0])

    visited = [[False] * w for _ in range(h)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs_island(si, sj):
        q = deque()
        q.append((si, sj))
        visited[si][sj] = True
        total = int(maps[si][sj])
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny]:
                    if maps[nx][ny] != 'X':
                        visited[nx][ny] = True
                        total += int(maps[nx][ny])
                        q.append((nx, ny))
        return total

    results = []
    for i in range(h):
        for j in range(w):
            if not visited[i][j] and maps[i][j] != 'X':
                results.append(bfs_island(i, j))

    if not results:
        return [-1]
    results.sort()
    return results
