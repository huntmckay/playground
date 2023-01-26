# point.py

class Point:

    def __new__(cls, *args, **kwargs):
        """
        method __new__ takes an undetermined amount of args that it will 
        pass to the initializer method
        """
        print("1. Create a new instance of Point.")
        return super().__new__(cls)

    def __init__(self, x, y):
        print("2. Initialize the new instance of Point.")
        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"{type(self).__name__}(x={self.x},y={self.y})"
        #str implementation of the class attributes
