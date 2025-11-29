import random
import math

class C1:

    def __init__(self, a1, a2, a3):
        self.cx = a2
        self.cy = a3
        self.rsq = a1 * a1

    def randPoint(self):
        while True:
            v1 = random.uniform(-math.sqrt(self.rsq), math.sqrt(self.rsq))
            v2 = random.uniform(-math.sqrt(self.rsq), math.sqrt(self.rsq))
            if v1 * v1 + v2 * v2 <= self.rsq:
                return (self.cx + v1, self.cy + v2)
