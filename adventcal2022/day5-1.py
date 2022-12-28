import array as arr
ff = open("input5", "r")


jj = [line.rstrip('\n') for line in ff]

lol = []

for i in jj[:9]:
    for i in  range(1,10):
        lol.append(i)

print(lol)
#take it each line as a list then make some sort of thing idk im tired good luck future me :)
