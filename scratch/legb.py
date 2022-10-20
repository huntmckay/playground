variable = 'global scope'
print(variable)
def enclosed():

    variable = 'enclosed scope'
    print(variable)

    def local():
        variable = 'local scope'
        print(variable)
    local()

enclosed()
