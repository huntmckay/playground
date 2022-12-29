#By listing the first six prime nbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
#What is the 10,001st prime nber?

def isPrime(n):
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return False
        else:
            return True
    else:
        return False


if __name__ == '__main__':
    pc = 0
    while pc < 10002:
        n = 1
        while n > 0:
            if isPrime(n) == True:
                print(n, 'is the', pc ,'prime')
                n += 1
                pc +=1
            else:
                n += 1

