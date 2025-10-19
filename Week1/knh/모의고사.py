def solution(answers):
    answer = []
    arr1 = [1, 2, 3, 4, 5]
    arr2 = [2, 1, 2, 3, 2, 4, 2, 5]
    arr3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    first = 0
    second = 0
    third = 0
    for i in range(len(answers)):
        if arr1[i % 5] == answers[i]:
            first += 1
        if arr2[i % 8] == answers[i]:
            second += 1
        if arr3[i % 10] == answers[i]:
            third += 1
    max_v = max(first, second, third)

    if max_v == first:
        answer.append(1)
    if max_v == second:
        answer.append(2)
    if max_v == third:
        answer.append(3)
    return answer