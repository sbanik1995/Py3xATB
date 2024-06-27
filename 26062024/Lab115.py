class Dog:
    name = None
    id = None


# Constructor? -> Use to initiate the values of the instance variable(attributes)

    def sleep(self):
        print("Sleeping doggy")


dog1 = Dog()
print(dog1.name)
dog1.name = "Django"
print(dog1.name)
dog1.sleep


dog2 = Dog()
print(dog2.name)
dog2.name = "Oskar"
print(dog2.name)
dog2.sleep

