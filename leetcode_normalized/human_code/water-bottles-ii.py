class C1(object):

    def maxBottlesDrunk(self, a1, a2):
        """
        """
        v1 = a1
        while a1 >= a2:
            a1 -= a2
            a2 += 1
            v1 += 1
            a1 += 1
        return v1
