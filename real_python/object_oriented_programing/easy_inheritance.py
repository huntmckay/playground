class Person:
    
    description = "general person"

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name} & I am {self.age} years old")
    def eat(self,food):
        self.food = food
        print(f"{self.name} eats {self.food}")
    
    def action(self):
        print(f"{self.name} jumps")

class Baby(Person):
    
    description = "baby"

    def speak(self):
        print("ba ba ba ba ba")
    
    def nap(self):
        print(f"{self.name} takes a nap")

person = Person("steve", 20)

person.speak()
person.eat("pasta")
person.action()

baby = Baby("Ian", 1)

baby.speak()
baby.eat("baby food")
baby.action()

print(person.description)
print(baby.description)

print(isinstance(baby, Person))
