import collections

class C1(object):

    def numberOfBoomerangs(self, a1):
        """
        """
        v1 = 0
        for v2 in range(len(a1)):
            v3 = collections.defaultdict(int)
            for v4 in range(len(a1)):
                if v4 == v2:
                    continue
                v5, v6 = (a1[v2][0] - a1[v4][0], a1[v2][1] - a1[v4][1])
                v3[v5 ** 2 + v6 ** 2] += 1
            for v7, v8 in v3.items():
                if v8 > 1:
                    v1 += v8 * (v8 - 1)
        return v1

    def numberOfBoomerangs2(self, a1):
        """
        """
        v1 = 0
        for v2, v3 in enumerate(a1):
            v4 = []
            for v5, v6 in enumerate(a1[:v2] + a1[v2 + 1:]):
                v4.append((v6[0] - v3[0]) ** 2 + (v6[1] - v3[1]) ** 2)
            for v7 in list(collections.Counter(v4).values()):
                if v7 > 1:
                    v1 += v7 * (v7 - 1)
        return v1
