def solution(phone_book):
    phone_book.sort()
    
    tmp = None
    for phone in phone_book:
        if not tmp:
            tmp = phone
            continue
        
        if tmp == phone[:len(tmp)]:
            return False
        
        tmp = phone
    
    return True