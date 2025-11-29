class C1:

    def maxProductDifference(self, a1):
        a1.sort()
        return a1[-1] * a1[-2] - a1[0] * a1[1]
