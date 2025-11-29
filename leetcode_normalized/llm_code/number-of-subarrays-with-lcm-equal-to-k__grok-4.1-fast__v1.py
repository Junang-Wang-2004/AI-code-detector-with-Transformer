import math
from collections import defaultdict

class C1:

    def subarrayLCM(self, a1, a2):

        def lcm(a1, a2):
            return a1 * a2 // math.gcd(a1, a2)
        v1 = defaultdict(int)
        v2 = 0
        for v3 in a1:
            if a2 % v3 != 0:
                v1.clear()
                continue
            v4 = defaultdict(int)
            v4[v3] += 1
            for v5, v6 in v1.items():
                v4[lcm(v5, v3)] += v6
            v1 = v4
            v2 += v1[a2]
        return v2
