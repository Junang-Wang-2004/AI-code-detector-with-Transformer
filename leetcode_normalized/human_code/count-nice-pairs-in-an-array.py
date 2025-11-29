import collections

class C1(object):

    def countNicePairs(self, a1):
        """
        """
        v1 = 10 ** 9 + 7

        def rev(a1):
            v1 = 0
            while a1:
                a1, v3 = divmod(a1, 10)
                v1 = v1 * 10 + v3
            return v1
        v2 = 0
        v3 = collections.defaultdict(int)
        for v4 in a1:
            v2 = (v2 + v3[v4 - rev(v4)]) % v1
            v3[v4 - rev(v4)] += 1
        return v2
