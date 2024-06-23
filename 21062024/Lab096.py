def my_decorator(func):
    def wrapper():
        print(" Starting ..... ")
        print(" ********* ")
        func()
        print(" ********* ")
        print(" Ending ")
    return wrapper()



@my_decorator
def say_hello():
    print("Say Hello")