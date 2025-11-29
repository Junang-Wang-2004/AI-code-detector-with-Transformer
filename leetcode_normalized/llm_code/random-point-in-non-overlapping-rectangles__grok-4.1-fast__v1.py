import random
import bisect

class C1:

    def __init__(self, a1):
        self.bounds = [list(r) for v1 in a1]
        self.areas = [0]
        for v2, v3, v4, v5 in a1:
            v6 = (v4 - v2 + 1) * (v5 - v3 + 1)
            self.areas.append(self.areas[-1] + v6)

    def pick(self):
        v1 = self.areas[-1]
        v2 = random.randint(0, v1 - 1)
        v3 = bisect.bisect_right(self.areas, v2) - 1
        v4 = v2 - self.areas[v3]
        v5 = self.bounds[v3]
        v6 = v4 % (v5[2] - v5[0] + 1)
        v7 = v4 // (v5[2] - v5[0] + 1)
        return [v5[0] + v6, v5[1] + v7]
