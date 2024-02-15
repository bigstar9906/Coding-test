from max36_1036 import MAX_36
    

def Test_1():
    if MAX_36("5\nGOOD\nLUCK\n\nAND\nHAVE\nFUN\n7") == "31YUB":
        return "Success for test_1"
    else : 
        return "Fail for test_1"
    
def Test_2():
    if MAX_36("1\nHELLO\n2") == "ZZLLO":
        return "Success for test_2"
    else : 
        return "Fail for test_2"

def Test_3():
    if MAX_36("5\n500\nPOINTS\nFOR\nTHIS\nPROBLEM\n5") == "110TC85":
        return "Success for test_3"
    else : 
        return "Fail for test_3"

def Test_4():
    if MAX_36("6\nTO\nBE\nOR\nNOT\nTO\nBE\n0") == "QNO":
        return "Success for test_4"
    else : 
        return "Fail for test_4"
    
def Test_5():
    if MAX_36("1\nKEQUALS36\n36") == "ZZZZZZZZZ":
        return "Success for test_5"
    else : 
        return "Fail for test_5"
    
Success = []
Success.append(Test_1())
Success.append(Test_2())
Success.append(Test_3())
Success.append(Test_4())
Success.append(Test_5())
print(Success)