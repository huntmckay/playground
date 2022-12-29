#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
# 1 create a list of consecutive integers from 2 thru n (2,3,4,...n)
# 2 let p = 2 at start the smallest prime number
# 3 enumerate the multiples of p by counting in increments of p and mark thme in a list 
# 4 find the smallest number in the list greater than p that is not marked

import math


def primefactors(n):
        
    while n % 2 == 0:
        print(2) 
        n = n /2

    # n must be odd at this point
    for i in range(3,int(math.sqrt(n))+1,2):

        while n % i == 0:
            print(i)
            n = n / i

    if n > 2:
        print(n)

n = 600851475143

primefactors(n)
