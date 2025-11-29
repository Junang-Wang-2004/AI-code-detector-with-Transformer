import collections

class C1(object):

    def subarraysWithKDistinct(self, a1, a2):
        """
        """

        def atMostK(a1, a2):
            v1 = collections.defaultdict(int)
            v2, v3 = (0, 0)
            for v4 in range(len(a1)):
                v1[a1[v4]] += 1
                while len(v1) > a2:
                    v1[a1[v3]] -= 1
                    if v1[a1[v3]] == 0:
                        v1.pop(a1[v3])
                    v3 += 1
                v2 += v4 - v3 + 1
            return v2
        return atMostK(a1, a2) - atMostK(a1, a2 - 1)
