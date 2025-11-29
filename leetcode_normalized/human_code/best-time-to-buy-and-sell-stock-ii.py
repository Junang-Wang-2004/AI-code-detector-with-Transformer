class C1(object):

    def maxProfit(self, a1):
        v1 = 0
        for v2 in range(len(a1) - 1):
            v1 += max(0, a1[v2 + 1] - a1[v2])
        return v1

    def maxProfit2(self, a1):
        return sum([max(a1[x + 1] - a1[x], 0) for v1 in range(len(a1[:-1]))])
