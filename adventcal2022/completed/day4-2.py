ff = open("input4", "r")

data = [line.rstrip('\n') for line in ff]
total = 0

def clean(a):

    r = []
    comma = a.split(',')
    for i in comma:
        dash = i.split('-')
        r.append(dash)

    r = r[0] + r[1] 
    r = [ int(x) for x in r ] 
    return r

def calc(r):
    
    r1 = [ x for x in range(r[0],r[1]+1) ]
    r2 = range(r[2],r[3]+1)

    # Need to compare list elements, any match
    # any match should return True

    print(f"{r[0]}-{r[1]},{r[2]}-{r[3]}")
    
    for i in r1:
        result = i in r2
        print(f'{i} in {r2} {result}')
        if result:
            return result
        
for i in data:
    
    r = clean(i)
    c = calc(r)
    if c:
        print('overlap',i,c)
        total = total + 1
    else:
        print('none   ',i,c)

print(total)
