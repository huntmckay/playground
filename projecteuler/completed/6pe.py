#The sum of the squares of the first ten natural numbers is, 1**2 + 2**2...10**2=285
#The square of the sum of the first ten natural numbers is,(1+2+...10)**2 == 55**2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
def sum_sqr():
    x= 0
    for i in range(1,101):
        x = x + (i ** 2)
    return x

def sqr_sum():
    j = 0
    for i in range(1,101):
        j = j + i 
    return j**2

print(sqr_sum() - sum_sqr())
