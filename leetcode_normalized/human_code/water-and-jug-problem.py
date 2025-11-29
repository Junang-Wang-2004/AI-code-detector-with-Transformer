class C1(object):

    def canMeasureWater(self, a1, a2, a3):
        """
        """

        def gcd(a1, a2):
            while a2:
                a1, a2 = (a2, a1 % a2)
            return a1
        return a3 == 0 or (a3 <= a1 + a2 and a3 % gcd(a1, a2) == 0)
