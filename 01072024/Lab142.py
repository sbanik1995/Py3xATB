class GF:
    def car(self):
        return "Old car"

class F(GF):
    def car(self):
        return "Honda civic"


class S(F):
    def car(self):
        return "Lambo"


son = S()
gf = GF()
print(gf.car())
print(son.car())
