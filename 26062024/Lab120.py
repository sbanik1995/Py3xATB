class Calc:
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def sum(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def mul(self):
        return self.a * self.b

    def div(self):
        return self.a / self.b


print(Calc(10,20).sum())
print(Calc(10,20).sub())
print(Calc(10,20).mul())
print(Calc(10,20).div())
