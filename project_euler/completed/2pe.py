# Fibonacci numbers module

#def fib(n): # write fib seq up to n
#    a, b = 0, 1
#    while a < n:
#        print(a, end=' ')
#        a, b = b, a + b
#    print()
def fib(n): # return fib seq up to n in list
    result = []
    result_even = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        if (a % 2) == 0:
            result_even.append(a)
        else:
            continue
    return sum(result_even) 

        

    # this is returning an empty list
    # need way to check for number even or odd before appended to list but not remove it from fib counter
    
