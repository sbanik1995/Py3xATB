class MyClass:
    def __init__(self):
        self.name = "Sourav"
        self._email = "abc@gmil.com"

    def public_func(self):
        print("Public Func()")

    def __private_func(self):
        print("You can only access me via an another method, this is private method")

    def public_fn_private(self):
        self.__private_func()
        print(self._email)


# Security -> Not everyone can access your variables / methods, f(n)

a = MyClass()
a.public_func()
a.public_fn_private()
