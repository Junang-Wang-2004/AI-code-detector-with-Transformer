import collections

class C1(object):

    def countPairs(self, a1, a2, a3):
        """
        """

        def count(a1, a2):
            v1 = 0
            v2 = collections.Counter(a1)
            while a2:
                if a2 & 1:
                    v1 += sum((v2[a2 ^ 1 ^ k] * v2[k] for v3 in v2.keys())) // 2
                v2 = collections.Counter({v3 >> 1: v2[v3] + v2[v3 ^ 1] for v3 in v2.keys()})
                a2 >>= 1
            return v1
        return count(a1, a3 + 1) - count(a1, a2)
