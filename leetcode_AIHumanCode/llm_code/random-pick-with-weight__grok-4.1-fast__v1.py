import random

class Solution:
    def __init__(self, weights):
        self.cumsum = []
        accum = 0
        for weight in weights:
            accum += weight
            self.cumsum.append(accum)
        self.total = accum

    def pickIndex(self):
        tgt = random.randrange(self.total)
        l, r = 0, len(self.cumsum) - 1
        while l < r:
            m = l + (r - l) // 2
            if self.cumsum[m] > tgt:
                r = m
            else:
                l = m + 1
        return l
