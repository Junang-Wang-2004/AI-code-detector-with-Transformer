import collections

class C1(object):

    def getDistances(self, a1):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            v1[v3].append(v2)
        v4 = [0] * len(a1)
        for v5 in v1.values():
            v6 = [0]
            for v2 in v5:
                v6.append(v6[-1] + v2)
            for v2, v7 in enumerate(v5):
                v4[v7] = v7 * (v2 + 1) - v6[v2 + 1] + (v6[len(v5)] - v6[v2] - v7 * (len(v5) - v2))
        return v4
