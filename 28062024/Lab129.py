class VWOLogin():
    def __init__(self, email, password, name):
        self.__email = email  # Added this line
        self.__password = password
        self.name = name
        self.__name = name

    def login_confirm(self):
        if self.__email == "abc@gmail.com" and self.__password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed to enter")


# This is end of class

page1 = VWOLogin("abc@gmail.com", "Pass123", "Sourav")
print(page1.name)
page1.login_confirm()
