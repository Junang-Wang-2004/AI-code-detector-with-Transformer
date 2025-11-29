MOD = 10**9 + 7

class Fancy:
    def __init__(self):
        self.data = []
        self.af_a = 1
        self.af_b = 0

    def append(self, val):
        inv = pow(self.af_a, MOD - 2, MOD)
        base = ((val - self.af_b) % MOD * inv) % MOD
        self.data.append(base)

    def addAll(self, inc):
        self.af_b = (self.af_b + inc) % MOD

    def multAll(self, m):
        self.af_a = (self.af_a * m) % MOD
        self.af_b = (self.af_b * m) % MOD

    def getIndex(self, idx):
        if idx >= len(self.data):
            return -1
        return (self.data[idx] * self.af_a + self.af_b) % MOD
