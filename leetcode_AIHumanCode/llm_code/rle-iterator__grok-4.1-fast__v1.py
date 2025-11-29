class RLEIterator:

    def __init__(self, encoding):
        self.encoding = encoding
        self.idx = 0
        self.used = 0

    def next(self, k):
        while self.idx < len(self.encoding):
            length = self.encoding[self.idx]
            left = length - self.used
            if k < left:
                self.used += k
                return self.encoding[self.idx + 1]
            k -= left
            self.used = 0
            self.idx += 2
        return -1
