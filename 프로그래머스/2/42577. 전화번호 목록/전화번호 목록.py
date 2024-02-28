def solution(phone_book):
    answer = True
    numlen = dict()
    phone_book.sort(key = lambda x:len(x))
    for num in phone_book:
        for length in range(1,len(num)+1):
            if length in numlen:
                if num[:length] in numlen[length]:
                    return False
        if len(num) in numlen:
            numlen[len(num)][num] = 1
        else :
            new = dict()
            new[num] = 1
            numlen[len(num)] = new        
    return answer