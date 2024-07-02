# Inheritance -> Acquirethe Attributes and Behaviour
# Data Members and Methods

# Inheritance Definition -> It is a concept in Object Oriented Programing(OOPs) that allows a class(Child Class) to inherit attributes and methods from another class (Parent Class)

# Types of Inheritance
# 1. Single Inheritance -> 80% -> API Automation and Web Automation -> 80% -> Single
# 2. Multiple Inheritance
# 3. Multilevel Inheritance
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance

# Single Inheritance

class Grandparent: #Parent Class
    key = "abc@123"
    def grandparent_method(self):
        return "This is a grandparent method"

class Father(Grandparent): #Child Class
    def parent_method(self):
        return "This is a parent method"

grandfather = Grandparent()
grandfather.grandparent_method()


parent = Father()
print(parent.parent_method())
print(parent.grandparent_method())
print(parent.key)
