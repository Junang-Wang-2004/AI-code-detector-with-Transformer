class ProductOfNumbers:

    def __init__(self):
        self.prefix = [1]

    def add(self, val):
        if val == 0:
            self.prefix = [1]
            return
        self.prefix.append(self.prefix[-1] * val)

    def getProduct(self, cnt):
        length = len(self.prefix)
        if length <= cnt:
            return 0
        return self.prefix[-1] // self.prefix[length - cnt - 1]
