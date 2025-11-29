import random

class C1:

    def __init__(self, a1):
        self.source = a1

    def reset(self):
        return self.source

    def shuffle(self):
        v1 = self.source[:]
        random.shuffle(v1)
        return v1
