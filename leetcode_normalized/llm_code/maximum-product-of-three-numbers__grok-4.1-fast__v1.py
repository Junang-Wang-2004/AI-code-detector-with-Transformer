class C1:

    def maximumProduct(self, a1):
        a1.sort()
        return max(a1[0] * a1[1] * a1[-1], a1[-3] * a1[-2] * a1[-1])
