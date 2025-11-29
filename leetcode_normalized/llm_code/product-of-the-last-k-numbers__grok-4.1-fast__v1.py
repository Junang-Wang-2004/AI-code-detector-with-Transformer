class C1:

    def __init__(self):
        self.prefix = [1]

    def add(self, a1):
        if a1 == 0:
            self.prefix = [1]
            return
        self.prefix.append(self.prefix[-1] * a1)

    def getProduct(self, a1):
        v1 = len(self.prefix)
        if v1 <= a1:
            return 0
        return self.prefix[-1] // self.prefix[v1 - a1 - 1]
