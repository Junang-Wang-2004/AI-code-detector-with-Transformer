import collections
import random
import bisect

class C1:

    def __init__(self, a1):
        self.values = a1
        self.indices = collections.defaultdict(list)
        for v1, v2 in enumerate(a1):
            self.indices[v2].append(v1)
        self.sample_count = 35

    def query(self, a1, a2, a3):
        for v1 in range(self.sample_count):
            v2 = random.randint(a1, a2)
            v3 = self.values[v2]
            v4 = self.indices[v3]
            v5 = bisect.bisect_right(v4, a2) - bisect.bisect_left(v4, a1)
            if v5 >= a3:
                return v3
        return -1
