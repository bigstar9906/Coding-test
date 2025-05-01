def solution(phone_book):
    phone_book = sorted(phone_book,key=lambda x: len(x))
    num_hash = dict()
    for num in phone_book:
        if len(num_hash)==0:
            num_hash[num]=1
        else:
            current=""
            for n in num:
                current+=n
                if current in num_hash:
                    return False
            num_hash[num]=1
    return True