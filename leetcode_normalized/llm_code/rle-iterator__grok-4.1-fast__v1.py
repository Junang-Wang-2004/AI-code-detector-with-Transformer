class C1:

    def __init__(self, a1):
        self.encoding = a1
        self.idx = 0
        self.used = 0

    def next(self, a1):
        while self.idx < len(self.encoding):
            v1 = self.encoding[self.idx]
            v2 = v1 - self.used
            if a1 < v2:
                self.used += a1
                return self.encoding[self.idx + 1]
            a1 -= v2
            self.used = 0
            self.idx += 2
        return -1
