class C1(object):

    def findMinFibonacciNumbers(self, a1):
        """
        """
        v1, v2, v3 = (0, 1, 1)
        while v3 <= a1:
            v3, v2 = (v2 + v3, v3)
        while a1:
            if v2 <= a1:
                a1 -= v2
                v1 += 1
            v2, v3 = (v3 - v2, v2)
        return v1
