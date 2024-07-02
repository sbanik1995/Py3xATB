# Method Overloading -> Not supported in Python

class MathUtils(object):
    def add(self, a, b=0, c=0):
        return a + b + c
    
    # def add(self, a, b)
    # pass


math = MathUtils()
op0 = math.add(1)
op1 = math.add(1, 2)
op2 = math.add(1, 2, 3)
print(op0, op1, op2)
