class C1(object):

    def maxProfit(self, a1):
        v1, v2 = (0, float('inf'))
        for v3 in a1:
            v2 = min(v2, v3)
            v1 = max(v1, v3 - v2)
        return v1
