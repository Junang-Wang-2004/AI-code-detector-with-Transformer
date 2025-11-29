import bisect

class C1(object):

    def fullBloomFlowers(self, a1, a2):
        """
        """
        v1, v2 = ([], [])
        for v3, v4 in a1:
            v1.append(v3)
            v2.append(v4 + 1)
        v1.sort()
        v2.sort()
        return [bisect.bisect_right(v1, t) - bisect.bisect_right(v2, t) for v5 in a2]
