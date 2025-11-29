import random

class Solution:

    def __init__(self, n_rows, n_cols):
        self.n_rows = n_rows
        self.n_cols = n_cols
        self.remaining = n_rows * n_cols
        self.remap = {}

    def flip(self):
        self.remaining -= 1
        k = random.randrange(self.remaining)
        pos = self.remap[k] if k in self.remap else k
        last = self.remap[self.remaining] if self.remaining in self.remap else self.remaining
        self.remap[k] = last
        row = pos // self.n_cols
        col = pos % self.n_cols
        return (row, col)

    def reset(self):
        self.remaining = self.n_rows * self.n_cols
        self.remap = {}
