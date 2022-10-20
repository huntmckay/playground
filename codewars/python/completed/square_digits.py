def square_digits(num):
    
    numList = [ x for x in str(num) ]
    outStr = ''
    for i in numList:
        jj = int(i)
        outStr = outStr+str(jj**2)
    
    return int(outStr)

# Test Cases
# 9119 == 811181
print(square_digits(9119))
