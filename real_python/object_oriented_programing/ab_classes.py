# ab_classes.py

class A:
    def __init__(self, a_value):
        print("Initialize the new instance of A.")
        self.a_value = a_value

class B:
    def __new__(cls, *args,**kwargs):
        return A(42)

    #B never initializes. Instances of b have a_value, but no b_value
    def __init__(self, b_value):
        print("Initialized the new instance of B.")
        self.b_value = b_value

def test():
    
    a = A(21)
    print(a.a_value)
    print(isinstance(a,A))

    b = B(21)
    print(b.b_value)
    print(isinstance(b,B))
    print(isinstance(b,A))
