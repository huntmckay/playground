ff = open("input3", "r")

rucks = [line.rstrip('\n') for line in ff]


def clean(ruck):
    
    assert type(ruck) is list, f"expected list, got {type(ruck)}"
 
    cleanruck = set(ruck) 
    cruck = cleanruck.pop()
    
    if cruck.isupper():
        return ord(cruck) - 38
    elif cruck.islower():
        return ord(cruck) - 96
    else:
        return 'ERROR'
total = 0
for ruck in rucks:

    rucklen = len(ruck)//2
    
    smruck = ruck[0:rucklen]
    bgruck = ruck[rucklen:]
    diffruck = [] 
    
    for i in bgruck:
        if i in smruck:
            diffruck.append(i)
    
    dr = clean(diffruck)
    total = total + dr
    print('full ruck: ',ruck)
    
    print('diff ruck: ',dr)
print('total priority: ', total)
