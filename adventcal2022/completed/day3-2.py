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

def divgroups(rucks, n):

    assert type(rucks) is list, f"expected list, got {type(rucks)}" 
    for i in range(0, len(rucks), n):
        yield rucks[i:i + n]

total = 0
n = 3
groups = list(divgroups(rucks, n))

for group in groups:
    badge = []
    for i in group[0]:
        if i in group[1] and i in group[2]:
            badge.append(i)
    total = total + clean(badge)

print(total)
