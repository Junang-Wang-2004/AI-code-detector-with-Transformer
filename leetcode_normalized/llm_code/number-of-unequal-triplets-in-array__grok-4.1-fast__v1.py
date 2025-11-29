import collections

class C1(object):

    def unequalTriplets(self, a1):
        v1 = collections.Counter(a1)
        v2 = len(a1)
        v3 = v2 * (v2 - 1) * (v2 - 2) // 6
        v4 = sum((f * (f - 1) * (f - 2) // 6 for v5 in v1.values()))
        v6 = sum((v5 * (v5 - 1) // 2 * (v2 - v5) for v5 in v1.values()))
        return v3 - v4 - v6
