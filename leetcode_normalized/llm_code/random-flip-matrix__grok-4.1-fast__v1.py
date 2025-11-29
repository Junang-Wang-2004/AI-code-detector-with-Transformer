import random

class C1:

    def __init__(self, a1, a2):
        self.n_rows = a1
        self.n_cols = a2
        self.remaining = a1 * a2
        self.remap = {}

    def flip(self):
        self.remaining -= 1
        v1 = random.randrange(self.remaining)
        v2 = self.remap[v1] if v1 in self.remap else v1
        v3 = self.remap[self.remaining] if self.remaining in self.remap else self.remaining
        self.remap[v1] = v3
        v4 = v2 // self.n_cols
        v5 = v2 % self.n_cols
        return (v4, v5)

    def reset(self):
        self.remaining = self.n_rows * self.n_cols
        self.remap = {}
