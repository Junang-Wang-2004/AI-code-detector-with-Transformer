class Bitset:

    def __init__(self, size):
        self.n = size
        self.values = [0] * size
        self.rev = 0
        self.ones = 0

    def fix(self, idx):
        curr = self.values[idx] ^ self.rev
        if curr == 0:
            self.ones += 1
        self.values[idx] = 1 ^ self.rev

    def unfix(self, idx):
        curr = self.values[idx] ^ self.rev
        if curr == 1:
            self.ones -= 1
        self.values[idx] = 0 ^ self.rev

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
        return ''.join(str(v ^ self.rev) for v in self.values)
