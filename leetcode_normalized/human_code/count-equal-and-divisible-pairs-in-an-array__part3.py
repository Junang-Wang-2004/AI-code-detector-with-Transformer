import collections

class C1(object):

    def countPairs(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(list)
        for v2, v3 in enumerate(a1):
            v1[v3].append(v2)
        return sum((idx[v2] * idx[j] % a2 == 0 for v4 in v1.values() for v2 in range(len(v4)) for v5 in range(v2 + 1, len(v4))))
