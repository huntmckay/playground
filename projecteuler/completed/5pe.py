
def modo(x):
    for i in range(1,21):
        if x % i == 0:
            continue
        else:
            return False
    return True

if __name__ == '__main__':
    num = 2520 
    while not modo(num):
        num += 2520
    print(num)
