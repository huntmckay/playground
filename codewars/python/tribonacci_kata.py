def tribonacci(signature, n):
    
    # sum last 3 positions starting with [1,1,1]
    c = 0
    outList = []
     
    for i in range(n+1):
        il = sum(signature[0:2])
        outList.append(il)
        signature.append(il)
        print(outList)
        del signature[0]       
    return outList 

print(tribonacci([1,1,1],10))
