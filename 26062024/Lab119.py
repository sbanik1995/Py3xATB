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

object_ref = Calc(20,10)
output1 = object_ref.sum()
output2 = object_ref.sub()
output3 = object_ref.mul()
output4 = object_ref.div()
print(output1)
print(output2)
print(output3)
print(output4)
