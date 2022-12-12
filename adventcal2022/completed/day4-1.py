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
    
    if r[0] <= r[2] and r[1] >= r[3]:
        return True
    if r[2] <= r[0] and r[3] >= r[1]:
        return True
    else:
        return False

for i in data:
    
    r = clean(i)
    c = calc(r)
    if c:
        total = total + 1
        print('no  lap',r)
    else:
        print('overlap',r)

print(total)
