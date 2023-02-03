# cars.py

class Car:

    def __init__(self, color, miles):
        self.color = color
        self.miles = miles

truck = Car("White", 150000)

print(f"my truck is {truck.color} and has {truck.miles} miles on it")
