v1 = 10 ** 9 + 7

class C1:

    def __init__(self):
        self.data = []
        self.af_a = 1
        self.af_b = 0

    def append(self, a1):
        v1 = pow(self.af_a, v1 - 2, v1)
        v2 = (a1 - self.af_b) % v1 * v1 % v1
        self.data.append(v2)

    def addAll(self, a1):
        self.af_b = (self.af_b + a1) % v1

    def multAll(self, a1):
        self.af_a = self.af_a * a1 % v1
        self.af_b = self.af_b * a1 % v1

    def getIndex(self, a1):
        if a1 >= len(self.data):
            return -1
        return (self.data[a1] * self.af_a + self.af_b) % v1
