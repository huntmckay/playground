def new():
    
    print('--- new function ---')

def animals(*args, sep="/"):
    return sep.join(args)

print(animals('dog','cat','parrot'))
print(animals('dog','cat','parrot',sep=':'))

new()

def food_type(dog,cat,parrot):
    print(dog)
    print(cat)
    print(parrot)

d = {'dog':'dry food','cat': 'wet food', 'parrot': 'idk worms'}
print(food_type(**d))


def document():

    """ 

    do nothing but doc

    """
    pass

print(document.__doc__)
