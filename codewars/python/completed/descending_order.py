def deo(num):
    mlist = [i for i in str(num)]
    r = sorted(mlist)
    return reverse(r)

print(deo(42145))
