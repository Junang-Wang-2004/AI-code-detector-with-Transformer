class C1:

    def __init__(self, a1):
        self.n = a1
        self.values = [0] * a1
        self.rev = 0
        self.ones = 0

    def fix(self, a1):
        v1 = self.values[a1] ^ self.rev
        if v1 == 0:
            self.ones += 1
        self.values[a1] = 1 ^ self.rev

    def unfix(self, a1):
        v1 = self.values[a1] ^ self.rev
        if v1 == 1:
            self.ones -= 1
        self.values[a1] = 0 ^ self.rev

    def flip(self):
        self.rev ^= 1
        self.ones = self.n - self.ones

    def all(self):
        return self.ones == self.n

    def one(self):
        return self.ones > 0

    def count(self):
        return self.ones

    def toString(self):
        return ''.join((str(v ^ self.rev) for v1 in self.values))
