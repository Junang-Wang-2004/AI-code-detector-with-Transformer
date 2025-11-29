import random

class C1:

    def __init__(self, a1, a2):
        self.count = a1 - len(a2)
        v1 = [num for v2 in a2 if v2 < self.count]
        v3 = {v2 for v2 in a2 if v2 >= self.count}
        self.swap = {}
        v4 = self.count
        for v5 in v1:
            while v4 in v3:
                v4 += 1
            self.swap[v5] = v4
            v4 += 1

    def pick(self):
        v1 = random.randint(0, self.count - 1)
        return self.swap.get(v1, v1)
