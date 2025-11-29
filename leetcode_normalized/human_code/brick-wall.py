import collections

class C1(object):

    def leastBricks(self, a1):
        """
        """
        v1 = collections.defaultdict(int)
        v2 = len(a1)
        for v3 in a1:
            v4 = 0
            for v5 in range(len(v3) - 1):
                v4 += v3[v5]
                v1[v4] += 1
                v2 = min(v2, len(a1) - v1[v4])
        return v2
