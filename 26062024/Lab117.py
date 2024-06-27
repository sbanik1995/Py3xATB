class Dog:
    name = None
    id = None

    def __init(self):
        print("Default No Argument")

    def __init__(self, name=None, id=None):
        self.name = name
        self.id = id

    def sleep(self):
        print("sleeping")



dog1 = Dog("Django", "1")
dog2 = Dog()
print(dog1.name)
print(dog1.id)
