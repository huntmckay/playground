'''
You are given an array (which will have a length of at least 3, 
        but could be very large) containing integers. The array is either 
entirely comprised of odd integers or entirely comprised of even 
integers except for a single integer N. Write a method that takes 
the array as an argument and returns this "outlier" N.
'''

def find_outlier(integers):

    odd = []
    even = []

    # newList = [ expression(element) for element in oldList if condition ] 
    odd = [ odd.append(x) for x in integers if x % 2 != 0 ]
    print(odd)
    even = [ even.append(x) for x in integers if x % 2 == 0 ]
    print(even)

    if len(odd) > len(even):
        return even
    else:
        return odd
    # Old version
    # for i in integers:
    #     if i % 2 == 0:
    #         even.append(i)
    #     else:
    #         odd.append(i)

    # if len(even) < len(odd):
    #     return even[0]
    # else:
    #     return odd[0]

# Tests

# Should return: 11 (the only odd number)
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))

# Should return: 160 (the only even number)
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
