# x = int
# y = base

jj=[]

# left for reminder that simple is better
# hex = {10:'A',11:'B',12:'C',13:'D',14:'E',15:'F'}
alpha ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def unary(x,y):

    for i in range(x):
        jj.append('I')
    r = "".join(jj)
    print(r)

def base(x,y):
    
    while(x>0):
        
        z = x % y
        jj.append(str(z))
        x=x//y
    jj.reverse()
    r = "".join(jj)
    print(r)

def bigbase(x,y):

    while(x>0):

        z = x % y
        if z >= 10:
            jj.append(str(alpha[z]))
        else:
            jj.append(str(z))
        x=x//y
    jj.reverse()
    r = "".join(jj)
    print(r)

# debug

x = int(input('number to convert: '))
y = int(input('base to convert to: '))

if y == 1:
    unary(x,y)
    print('ah, yes the old scriptures')

elif 1 < y < 11:
    base(x,y)

else:
    bigbase(x,y)
