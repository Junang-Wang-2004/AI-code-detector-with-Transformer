import collections

class C1:

    def countCompleteSubarrays(self, a1):
        v1 = len(a1)
        v2 = len(set(a1))
        v3 = collections.Counter()
        v4 = 0
        v5 = 0
        v6 = 0
        for v7 in range(v1):
            while v6 < v1 and v4 < v2:
                v3[a1[v6]] += 1
                if v3[a1[v6]] == 1:
                    v4 += 1
                v6 += 1
            if v4 == v2:
                v5 += v1 - v6 + 1
            v3[a1[v7]] -= 1
            if v3[a1[v7]] == 0:
                v4 -= 1
        return v5
