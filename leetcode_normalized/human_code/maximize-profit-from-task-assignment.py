import collections

class C1(object):

    def maxProfit(self, a1, a2):
        """
        """
        v1 = collections.defaultdict(int)
        for v2 in a1:
            v1[v2] += 1
        a2.sort(key=lambda x: v2[1], reverse=True)
        v3 = 0
        v4 = 1
        for v5, v6 in a2:
            if v1[v5]:
                v1[v5] -= 1
                v3 += v6
            elif v4:
                v4 -= 1
                v3 += v6
        return v3
