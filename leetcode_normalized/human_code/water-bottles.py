class C1(object):

    def numWaterBottles(self, a1, a2):
        """
        """
        v1 = a1
        while a1 >= a2:
            a1, v3 = divmod(a1, a2)
            v1 += a1
            a1 += v3
        return v1
