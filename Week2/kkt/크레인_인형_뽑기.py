from collections import deque

def solution(board, moves):
    n = len(board)
    board_queue = [deque() for i in range(n)]
    for i in range(n):
        for j in range(n):
            if not board[j][i] == 0:
                board_queue[i].append(board[j][i])
        
    basket = []
    answer= 0
    for move in moves:
        if board_queue[move-1]:
            x = board_queue[move-1].popleft()
            
            if basket and basket[-1] == x:
                basket.pop()
                answer += 2
                
            else:
                basket.append(x)
            
    return answer