def solution(n, computers):
    visited = [False] * n

    def dfs(start):
        stack = [start]
        visited[start] = True
        while stack:
            v = stack.pop()
            for u in range(n):
                if computers[v][u] == 1 and not visited[u]:
                    visited[u] = True
                    stack.append(u)

    networks = 0
    for i in range(n):
        if not visited[i]:
            dfs(i)
            networks += 1
    return networks