class Dog:

    species = "mammal"

    def __init__(self, name, age):
        """
            The init method is called when the object is initialized.
            Instance attributes are unique to each object created.
            name and age are parameters to be passed into the object instance
            self is a special keyword refering to the object being created
            species is a class attribute
        """
        self.name = name
        self.age = age

    def __str__(self):
        
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        
        return f"{self.name} says {sound}"

    def birthday(self):
        
        self.age += 1

class Monkey(Dog):
    
    def speak(self,sound):

        return f"{self.name} screams upper({sound})"

charlie = Monkey("Charlie", 10)
charlie.speak = "oooh ahhh ahhh"

dwayne = Dog("Dwayne", 2)
dwayne.speak = "arf"

print(charlie,charlie.speak)
print(dwayne,dwayne.speak)
