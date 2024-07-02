# Abstraction -> Hiding the details and showing what is required.

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

dog = Dog("Django")
print(dog.sound())

cat = Cat("Kitty")
print(cat.sound())
