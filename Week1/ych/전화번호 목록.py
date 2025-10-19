def solution(phone_book):
    phone_book.sort()
    
    for i in range(len(phone_book)):
        # 접두사가 있는 경우만 있으면 false니까 비교해서 같자마자 return false
        if i != len(phone_book) - 1 and phone_book[i + 1][:len(phone_book[i])] == phone_book[i]:
            return False
            
    answer = True
    return answer
