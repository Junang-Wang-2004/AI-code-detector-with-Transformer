from collections import Counter

class C1:

    def leastBricks(self, a1):
        v1 = Counter()
        for v2 in a1:
            v3 = 0
            for v4 in v2[:-1]:
                v3 += v4
                v1[v3] += 1
        v5 = max(v1.values(), default=0)
        return len(a1) - v5
