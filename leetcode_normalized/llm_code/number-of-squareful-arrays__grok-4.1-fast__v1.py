import collections
import math
from collections import defaultdict

class C1:

    def numSquarefulPerms(self, a1):

        def valid_sum(a1, a2):
            v1 = a1 + a2
            v2 = int(math.sqrt(v1))
            return v2 * v2 == v1
        v1 = collections.Counter(a1)
        v2 = defaultdict(list)
        for v3 in list(v1):
            for v4 in list(v1):
                if valid_sum(v3, v4):
                    v2[v3].append(v4)
        v5 = 0

        def search(a1, a2):
            nonlocal ans
            if a2 == 0:
                v1 += 1
                return
            for v2 in v2[a1]:
                if v1[v2] > 0:
                    v1[v2] -= 1
                    search(v2, a2 - 1)
                    v1[v2] += 1
        v6 = len(a1)
        for v7 in list(v1):
            if v1[v7] > 0:
                v1[v7] -= 1
                search(v7, v6 - 1)
                v1[v7] += 1
        return v5
