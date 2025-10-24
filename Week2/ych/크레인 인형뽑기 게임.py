def solution(board, moves):
    # board에는 2차원 배열 board[i]에는 한 열에 들어가 있는 인형들
    # moves에는 board[i]에서 i에 해당하는 열
    # moves를 다 돌아서
    # moves[i]에 해당하는 board[moves[i]].pop() 해가지고 lst에 넣는다.
    # 만약 board[moves[i]].pop()한 값이 lst[-1]에 있는거랑 같으면
    # 터진 인형 카운트 cnt += 2 하고, lst[-1].pop() 해버린다.
    # 아니면 lst.append(board[moves[i]].pop())

    lst = []
    cnt = 0
    for move in moves:
        col = move - 1
        
        for row in range(len(board)):
            if board[row][col] != 0:
                doll = board[row][col]
                board[row][col] = 0
                
                if lst and lst[-1] == doll:
                    lst.pop()
                    cnt += 2
                else:
                    lst.append(doll)
                break
    
    answer = cnt
    return answer
