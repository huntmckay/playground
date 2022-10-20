jj=[]
alpha ='0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def base(x,y):
    
    if y < 2:
        for i in range(x): jj.append('I')
    else:
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

x = int(input('number to convert: '))
y = int(input('base to convert to: '))
base(x,y)
