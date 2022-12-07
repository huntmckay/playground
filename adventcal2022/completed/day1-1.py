#!/usr/bin/python3


def bigger(num, newnum):
    
    if num < newnum:
        num = newnum

    return num

ff = open("day1input", "r")

jj = [line.rstrip('\n') for line in ff]

num = 0
big = 0
for i in jj:
    
    if i != '':
        num = num + int(i)
    else:
        big = bigger(num, big)
        num = 0

print(big)
