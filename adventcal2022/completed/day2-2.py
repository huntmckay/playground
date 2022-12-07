ff = open("input2", "r")

games = [line.rstrip('\n') for line in ff]

def value(pick):
   
    if pick == 'A' or pick == 'X':
        pick = 'rock' 
        val = 1   

    elif pick == 'B' or pick == 'Y':
        pick = 'paper'
        val = 2

    else:
        pick = 'scissors'
        val = 3

    return pick,val 

def outcome(sp,fp):
    
    if sp == 'X':
        if fp == 'rock':
            sp = 'Z' 
        elif fp == 'paper':
            sp = 'X'
        else:
            sp = 'Y' 

    elif sp == 'Y':
        if fp == 'rock':
            sp = 'X' 
        elif fp == 'paper':
            sp = 'Y'
        else:
            sp = 'Z' 

    elif sp == 'Z':
        if fp == 'rock':
            sp = 'Y' 
        elif fp == 'paper':
            sp = 'Z'
        else:
            sp = 'X' 

    return sp

def calcgame(game):
    
    win = 6
    draw = 3
    loss = 0
    # split into list with two items
    pick = game.split(' ')
    
    fp = value(pick[0])
    presp = pick[1]
    r = outcome(presp,fp[0]) 
    sp = value(r)
    
    if fp[0] == sp[0]:
        
        return sp[1] + draw
    
    elif fp[0] == 'rock':
        if sp[0] == 'paper':
            return sp[1] + win
        else: 
            return sp[1] + loss 

    elif fp[0] == 'paper':
        if sp[0] == 'scissors':
            return sp[1] + win
        else: 
            return sp[1] + loss 

    elif fp[0] == 'scissors':
        if sp[0] == 'rock':
            return sp[1] + win
        else: 
            return sp[1] + loss 
    else:
        breakpoint()

total = 0
for game in games:
    
    g = calcgame(game)
    total = total + g
print(total)
