class MyCustomException(Exception):
    def __in__init__(self, message):
        self.message = message
        super().__init__(message)

balance = 100

withdraw = int(input("Enter the amount to withdraw\n"))
if withdraw > balance:
    raise Exception("Balance is low")
else:
    print("Remain Bal" , (balance-withdraw))

