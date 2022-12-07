ff = open("input4", "r")

jj = [line.rstrip('\n') for line in ff]


def makerange(num):
    
    xx = jj[0].split(',') 

    for i in xx:
        
        yy = i.split('-')
        a = int(yy[0])
        b = int(yy[1])
        bb = range(a,b)
        print(len(bb))
