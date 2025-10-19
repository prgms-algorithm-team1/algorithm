def solution(answers):
    # 수포자들의 방식을 패턴화
    first_pattern = [1, 2, 3, 4, 5]
    second_pattern = [2, 1, 2, 3, 2, 4, 2, 5]
    third_pattern = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    # answers에 담긴 값들을 하나하나 돌면서 비교
    a = pattern_calc(answers, first_pattern)
    b = pattern_calc(answers, second_pattern)
    c = pattern_calc(answers, third_pattern)
    
    standard = max(a, b, c)
    
    answer = []
    scores = [a, b, c]
    for idx in range(3):
        if scores[idx] == standard:
            answer.append(idx + 1)
    
    return answer

def pattern_calc(answers, pattern):
    count = 0
    for i in range(len(answers)):
        if answers[i] == pattern[i % len(pattern)]:
            count += 1
    
    return count