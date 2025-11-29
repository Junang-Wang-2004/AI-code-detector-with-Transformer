import collections

class C1(object):

    def numberOfPairs(self, a1, a2, a3):
        """
        """
        v1 = [0] * (max(a1) + 1)
        for v2, v3 in collections.Counter((a3 * v2 for v2 in a2)).items():
            for v4 in range(1, (len(v1) - 1) // v2 + 1):
                v1[v4 * v2] += v3
        return sum((v1[v2] for v2 in a1))
