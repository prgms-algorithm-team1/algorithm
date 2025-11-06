def solution(k, dungeons):
    n = len(dungeons)
    visited = [False] * n
    def DFS(k,cnt):
        max_cnt = cnt
        for i in range(n):
            if not visited[i] and k >= dungeons[i][0]:
                visited[i] = True
                max_cnt = max(max_cnt, DFS(k - dungeons[i][1], cnt + 1))
                visited[i] = False
        return max_cnt
    
    answer = DFS(k,0)
    return answer