def solution(board, moves):
    answer = 0
    stack = []
    N = len(board)
    for move in moves:
        for i in range(N):
            if board[i][move - 1] > 0:
                if stack:
                    # stack에 마지막 인형과 크레인이 집은 인형이 같을 경우
                    if board[i][move - 1] == stack[-1]:
                        # stack에 인형 없앰
                        stack.pop()
                        # 크레인으로 집은 인형 없앰
                        board[i][move - 1] = 0
                        # 총 두개의 인형이 사라지고 결과에 2를 더함
                        answer += 2
                        break
                    else:
                        # 크레인이 집은 인형을 스택에 넣음
                        stack.append(board[i][move - 1])
                        board[i][move - 1] = 0
                        break
                else:
                    stack.append(board[i][move - 1])
                    board[i][move - 1] = 0
                    break
    return answer