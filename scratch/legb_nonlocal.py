x = 40

def h():

    x = 20

    def g():
        nonlocal x
        x = 100

    g()
    print(x)

h()
