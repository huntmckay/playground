jj = [2000001]
def decider(n,jj):
    while n > 1:
        if n % 2 == 0:
            n = n / 2
            jj.append(n)
        else:
            n = n * 3 + 1
            jj.append(n)
    return jj
print(len(decider(jj[0],jj)),decider(jj[0],jj))
