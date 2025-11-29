import random

class Solution:
    def __init__(self, N, blacklist):
        self.count = N - len(blacklist)
        lows = [num for num in blacklist if num < self.count]
        highs = {num for num in blacklist if num >= self.count}
        self.swap = {}
        next_avail = self.count
        for low in lows:
            while next_avail in highs:
                next_avail += 1
            self.swap[low] = next_avail
            next_avail += 1

    def pick(self):
        cand = random.randint(0, self.count - 1)
        return self.swap.get(cand, cand)
