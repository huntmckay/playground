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

    def description(self):
        
        return f"{self.name} is {self.age} years old"
    
    def speak(self, sound):
        
        return f"{self.name} says {sound}"

    def birthday(self):
        
        self.age += 1

mikey = Dog("mikey", 6)

for i in range(1,5):
    
    mikey.birthday()
    print(mikey.description(),mikey.speak("bark"))
