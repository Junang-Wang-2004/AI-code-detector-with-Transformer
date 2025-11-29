import random
import collections

class C1:

    def __init__(self, a1):
        self.index_map = collections.defaultdict(list)
        for v1 in range(len(a1)):
            v2 = a1[v1]
            self.index_map[v2].append(v1)

    def pick(self, a1):
        v1 = self.index_map[a1]
        return v1[random.randrange(len(v1))]
