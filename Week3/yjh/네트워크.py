def solution(n, computers):
    answer = 0
    visited = [False for i in range(n)]
    count=0
    for i in range(n):
        if visited[i]:
            pass
        else:
            count+=1
            stack = [i]
            while stack:
                x = stack.pop()
                visited[x] = True
                for j in range(n):
                    if computers[x][j] == 1 and not visited[j]:
                        stack.append(j)
    
    return count