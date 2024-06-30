class Person:
    # Class Variables / instance variables
    name = "Sourav"
    age = None


    def walk(self):
        a = 10 #Local Variable
        print("Person is walking")
        print("Hi", self.age)



sourav = Person()
sourav.walk()
