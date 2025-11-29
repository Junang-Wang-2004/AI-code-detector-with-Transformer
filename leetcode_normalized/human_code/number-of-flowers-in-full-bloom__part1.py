import bisect

class C1(object):

    def fullBloomFlowers(self, a1, a2):
        """
        """
        v1 = collections.Counter()
        for v2, v3 in a1:
            v1[v2] += 1
            v1[v3 + 1] -= 1
        v4 = sorted(v1.keys())
        v5 = [0]
        for v6 in v4:
            v5.append(v5[-1] + v1[v6])
        return [v5[bisect.bisect_right(v4, t)] for v7 in a2]
