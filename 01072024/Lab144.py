# Method overriding -> Same name in the parent and child. Child will always override the parent function
# Super function -> Calls the parent function

class Father:
    def home(self):
        print("1BHK")

class Son(Father):
    def home(self):
        super().home()
        print("No house")


sourav = Son()
sourav.home()
