#!/usr/bin/python3

ff = open("day1input", "r")

jj = [line.rstrip('\n') for line in ff]

num = 0
sumlist = []

for i in jj:
    
    if i != '':
        num = num + int(i)
    else:
        sumlist.append(num)
        num = 0
    topthree = sorted(sumlist, reverse=True) 
    tts = sum(topthree[0:3]) 

print(tts)
