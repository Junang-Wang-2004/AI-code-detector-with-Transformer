class C1(object):

    def shoppingOffers(self, a1, a2, a3):
        """
        """

        def shoppingOffersHelper(a1, a2, a3, a4):
            if a4 == len(a2):
                return sum(map(lambda x, y: x * y, a1, a3))
            v1 = shoppingOffersHelper(a1, a2, a3, a4 + 1)
            for v2 in range(len(a3)):
                a3[v2] -= a2[a4][v2]
            if all((need >= 0 for v3 in a3)):
                v1 = min(v1, a2[a4][-1] + shoppingOffersHelper(a1, a2, a3, a4))
            for v2 in range(len(a3)):
                a3[v2] += a2[a4][v2]
            return v1
        return shoppingOffersHelper(a1, a2, a3, 0)
