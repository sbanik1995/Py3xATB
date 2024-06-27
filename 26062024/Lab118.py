class Calc:
    def __init__(self):
        print("Hello DC")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


object_ref = Calc()
output1 = object_ref.sum(10, 20)
output2 = object_ref.sub(10, 20)
output3 = object_ref.mul(10, 20)
output4 = object_ref.div(10, 20)
print(output1)
print(output2)
print(output3)
print(output4)


