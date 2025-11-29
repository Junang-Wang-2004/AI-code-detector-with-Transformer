class C1(object):

    def brokenCalc(self, a1, a2):
        """
        """
        v1 = 0
        while a1 < a2:
            if a2 % 2:
                a2 += 1
            else:
                a2 /= 2
            v1 += 1
        return v1 + a1 - a2
