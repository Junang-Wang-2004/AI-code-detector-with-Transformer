import bisect

class C1(object):

    def minAbsDifference(self, a1, a2):
        """
        """
        v1, v2 = (sum((x for v3 in a1 if v3 > 0)), sum((v3 for v3 in a1 if v3 < 0)))
        if a2 > v1:
            return a2 - v1
        if a2 < v2:
            return v2 - a2
        v4 = abs(a2)
        v5 = set([0])
        for v6 in range(len(a1) // 2):
            for v3 in list(v5):
                if v3 + a1[v6] in v5:
                    continue
                v5.add(v3 + a1[v6])
                v4 = min(v4, abs(a2 - v3 - a1[v6]))
        v7 = sorted(v5)
        v8 = set([0])
        for v6 in range(len(a1) // 2, len(a1)):
            for v3 in list(v8):
                if v3 + a1[v6] in v8:
                    continue
                v8.add(v3 + a1[v6])
                v9 = bisect.bisect_left(v7, a2 - v3 - a1[v6])
                if v9 < len(v7):
                    v4 = min(v4, abs(a2 - v3 - a1[v6] - v7[v9]))
                if v9 > 0:
                    v4 = min(v4, abs(a2 - v3 - a1[v6] - v7[v9 - 1]))
                if v4 == 0:
                    return v4
        return v4
