
j = []

for x in range(10,100):
    for y in range(10,100):
        number = x*y
        z = list(str(number))
    if z == z[::-1]:
        print(z[::])
        j.append(z)
print(j[-1])
    #multiply by each number of the list return big list, tell it to fuck off based on index[0] inex[-1]
