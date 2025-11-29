class Cashier:

    def __init__(self, n, discount, products, prices):
        self.period = n
        self.disc_rate = discount / 100.0
        self.count = 0
        self.prices = dict(zip(products, prices))

    def getBill(self, items, counts):
        self.count = (self.count + 1) % self.period
        total = 0.0
        for i in range(len(items)):
            total += self.prices[items[i]] * counts[i]
        if self.count == 0:
            total *= (1 - self.disc_rate)
        return total
