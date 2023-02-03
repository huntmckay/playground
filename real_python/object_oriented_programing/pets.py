# pets.py

from random import choice

class Pet:
    def __new__(cls):
        other = choice([Dog, Cat, Python])
        instance = super().__new__(other)
        print(f"I'm a {type(instance).__name__}!")
        return instance

    def __init__(self):
        print("Never runs!")

class Dog:
    def communicate(self):
        print("woof! woof!")

class Cat:
    def communicate(self):
        print("meow! meow!")

class Python:
    def communicate(self):
        print("hiss! hiss!")
