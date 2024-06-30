class BankAccount:
    def __init__(self):
        self.balance = 0
        self.__private_var = 100

    def public_fn(self):
        print(self.__private_var)

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def show_balance(self):
        print("Your balance is: ", self.balance)

    def if_you_are_auth(self, flag):
        if flag:
            self.show_balance()
        else:
            print("Not Allowed")

    def if_you_are_auth_user(self, auth, amount):
        if auth:
            self.withdraw(amount)
        else:
            print("Not Allowed")


jp_chase = BankAccount()
jp_chase.deposit(101)

secret_pass = input("Enter your PIN to see Balance: ")
if secret_pass == "1234":
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth(False)

secret_pass = input("Enter your PIN to withdraw: ")
your_amount = int(input("Enter amount to withdraw: "))

if secret_pass == "1234":
    jp_chase.if_you_are_auth_user(True, amount=your_amount)
    jp_chase.if_you_are_auth(True)
else:
    jp_chase.if_you_are_auth_user(False, amount=your_amount)
