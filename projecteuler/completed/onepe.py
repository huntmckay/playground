x = 0
a = 0
y = [] 
b = []
while x < 1000:
    y.append(x)
    x += 3
#print(y)

while a < 1000:
    b.append(a)
    a += 5
#print(b)

y.extend(b)
print(sum(set(y)))
