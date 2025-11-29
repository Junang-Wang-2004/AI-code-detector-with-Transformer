class C1(object):

    def minSteps(self, a1):
        """
        """
        v1 = 0
        v2 = 2
        while v2 ** 2 <= a1:
            while a1 % v2 == 0:
                v1 += v2
                a1 //= v2
            v2 += 1
        if a1 > 1:
            v1 += a1
        return v1
