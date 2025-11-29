import collections
import itertools

class C1(object):

    def minAreaFreeRect(self, a1):
        """
        """
        a1.sort()
        a1 = [complex(*z) for v2 in a1]
        v3 = collections.defaultdict(list)
        for v4, v5 in itertools.combinations(a1, 2):
            v3[v4 - v5].append((v4 + v5) / 2)
        v6 = float('inf')
        for v7, v8 in v3.items():
            for v4, v5 in itertools.combinations(v8, 2):
                if v7.real * (v4 - v5).real + v7.imag * (v4 - v5).imag == 0.0:
                    v6 = min(v6, abs(v7) * abs(v4 - v5))
        return v6 if v6 < float('inf') else 0.0
