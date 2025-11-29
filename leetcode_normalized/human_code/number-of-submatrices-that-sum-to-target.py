import collections

class C1(object):

    def numSubmatrixSumTarget(self, a1, a2):
        """
        """
        if len(a1) > len(a1[0]):
            return self.numSubmatrixSumTarget(list(map(list, list(zip(*a1)))), a2)
        for v1 in range(len(a1)):
            for v2 in range(len(a1[v1]) - 1):
                a1[v1][v2 + 1] += a1[v1][v2]
        v3 = 0
        for v1 in range(len(a1)):
            v4 = [0] * len(a1[v1])
            for v2 in range(v1, len(a1)):
                v5 = collections.defaultdict(int)
                v5[0] = 1
                for v6 in range(len(a1[v2])):
                    v4[v6] += a1[v2][v6]
                    if v4[v6] - a2 in v5:
                        v3 += v5[v4[v6] - a2]
                    v5[v4[v6]] += 1
        return v3
