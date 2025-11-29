class C1:

    def __init__(self, a1, a2, a3, a4):
        self.period = a1
        self.disc_rate = a2 / 100.0
        self.count = 0
        self.prices = dict(zip(a3, a4))

    def getBill(self, a1, a2):
        self.count = (self.count + 1) % self.period
        v1 = 0.0
        for v2 in range(len(a1)):
            v1 += self.prices[a1[v2]] * a2[v2]
        if self.count == 0:
            v1 *= 1 - self.disc_rate
        return v1
