j = []
rr = []
for x in range(100,1000):
    for y in range(100,1000):
        number = x*y
        z = list(str(number))
        if z == z[::-1] and z[0] == '9':
            j.append(z)
for x in j:
    jj = map(''.join, j)
    zz = list(jj)
for i in zz:
    if len(i) <= 5:
        #print('if grabed i len =', len(i))
        continue
    else:
        #print('else grabed i len =', len(i))
        rr.append(i)
print(rr)
