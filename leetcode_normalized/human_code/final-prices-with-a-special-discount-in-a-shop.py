class C1(object):

    def finalPrices(self, a1):
        """
        """
        v1 = []
        for v2, v3 in enumerate(a1):
            while v1 and a1[v1[-1]] >= v3:
                a1[v1.pop()] -= v3
            v1.append(v2)
        return a1
