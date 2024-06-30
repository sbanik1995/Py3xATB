# Web Automation - Selenium
# Page - You are going to automate


class VWOLoginPage:
    email = None
    password = None

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def login_confirm(self):
        if self.password == "Pass123":
            print("Allowed to enter")
        else:
            print("Not allowed to enter")


# This is end of the class

sourav = VWOLoginPage("sourav@gmail.com", "123")
sourav.login_confirm()

amit = VWOLoginPage("amit@gmail.com", "Pass123")
amit.login_confirm()
