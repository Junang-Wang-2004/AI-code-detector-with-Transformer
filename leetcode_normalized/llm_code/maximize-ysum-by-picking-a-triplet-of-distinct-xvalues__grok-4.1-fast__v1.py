class C1(object):

    def maxSumDistinctTriplet(self, a1, a2):
        v1 = {}
        for v2, v3 in zip(a1, a2):
            if v2 not in v1 or v3 > v1[v2]:
                v1[v2] = v3
        v4 = list(v1.values())
        if len(v4) < 3:
            return -1
        v4.sort(reverse=True)
        return sum(v4[:3])
