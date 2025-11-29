import bisect
from itertools import permutations

class C1:

    def nextBeautifulNumber(self, a1):
        v1 = []
        for v2 in range(1, 1 << 9):
            v3 = []
            v4 = 0
            for v5 in range(1, 10):
                if v2 & 1 << v5 - 1:
                    v3.extend([str(v5)] * v5)
                    v4 += v5
            if v4 > 7 or v4 == 0:
                continue
            v6 = set(permutations(v3))
            for v7 in v6:
                v8 = int(''.join(v7))
                v1.append(v8)
        v1 = sorted(set(v1))
        v9 = bisect.bisect_right(v1, a1)
        return v1[v9]
