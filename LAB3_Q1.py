def Multiply(NUM):
    num=1
    for i in NUM:
       num*=i
    return num
numbers=[8,2,3,-1,7]
RESULTIS=Multiply(numbers)
print("RESULT is :",RESULTIS)
